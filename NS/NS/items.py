# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    info=scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    stock=scrapy.Field()
    manufacturer=scrapy.Field()
    description=scrapy.Field()
    delivery_info=scrapy.Field()
    review=scrapy.Field()
    pass
