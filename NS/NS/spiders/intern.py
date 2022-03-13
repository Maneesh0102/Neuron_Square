import scrapy
from ..items import NsItem
from scrapy.http.request import Request

class InternSpider(scrapy.Spider):
    name = 'intern'
    # allowed_domains = ['www.midsouthshooterssupply.com']
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?itemsperpage=60']

    def parse(self, response):
        links=[]
        temp=response.css('.catalog-item-name')
        for i in temp:
            link='https://www.midsouthshooterssupply.com/'+i.css('::attr(href)').extract()[0]
            links.append(link)
        for j in links:
            info=NsItem()
            request=Request(j,callback=self.parse_info)
            request.meta['info']=info
            yield request

    def parse_info(self,response):
        info=response.meta['info']
        price = response.css('#product-main .price span').css('::text').extract()[0]
        info['price'] = float(price[1:])
        name=response.css('.product-name').css('::text').extract()[0]
        info['title']=name
        status=response.css('.out-of-stock').css('::text').extract()[0]
        if status=='Out of Stock':
            info['stock']=False
        else:
            info['stock']=True
        manufact=response.css('.catalog-item-brand-item-number a ::text').extract()[0]
        info['manufacturer']=manufact
        desc=response.css('#description ::text').extract()
        temp=''
        for i in range(2,len(desc)):
            temp+=desc[i].strip()
            temp+='__'
        temp=temp[:-2]
        info['description']=temp
        del_info=response.css('#delivery-info ::text').extract()
        del_info=del_info[1:-1]
        temp=''
        for i in del_info:
            temp+=i
            temp+='__'
        temp=temp[:-2]
        info['delivery_info']=temp
        yield info
        pass
