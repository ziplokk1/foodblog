# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import Crawler
from ..items import ScraperItem


class IamafoodblogSpider(scrapy.Spider):
    name = 'iamafoodblog'
    allowed_domains = ['iamafoodblog.com']
    start_urls = ['https://iamafoodblog.com/category-sitemap.xml']

    def parse_post(self, response):
        content = response.xpath('//div[@class="post-container recipe-body"]/p/text()').extract()
        ingredients = ' '.join(response.xpath('//strong[@itemprop="recipeIngredient"]/text()').extract())
        item = ScraperItem()
        item['post_content'] = content
        item['title'] = response.meta['title']
        item['summary'] = response.xpath('//div[@class="post-teaser"]/text()').extract()
        item['ingredients'] = ingredients
        return item

    def parse_category(self, response):
        for a in response.xpath('//a[@title]'):
            href = a.xpath('./@href').extract()[0]
            title = a.xpath('./h4/text()').extract()
            yield response.follow(href, callback=self.parse_post, meta={'title': title})

    def parse(self, response):
        for href in response.xpath('//a:urlset/a:url/a:loc/text()', namespaces={'a': 'http://www.sitemaps.org/schemas/sitemap/0.9'}).extract():
            yield response.follow(href, callback=self.parse_category)
