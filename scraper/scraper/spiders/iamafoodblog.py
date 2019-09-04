# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import Crawler
from ..items import ScraperItem


class IamafoodblogSpider(scrapy.Spider):
    name = 'iamafoodblog'
    allowed_domains = ['iamafoodblog.com']
    start_urls = ['https://iamafoodblog.com/category/recipes/']

    def parse_post(self, response):
        content = response.xpath('//div[@class="post-container recipe-body"]/p/text()').extract()
        item = ScraperItem()
        item['post_content'] = content
        return item

    def parse(self, response):
        for href in response.xpath('//a/@href').extract():
            yield response.follow(href, callback=self.parse_post)
