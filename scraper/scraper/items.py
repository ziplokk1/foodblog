# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_content = scrapy.Field()
    title = scrapy.Field()
    ingredients = scrapy.Field()
    summary = scrapy.Field()