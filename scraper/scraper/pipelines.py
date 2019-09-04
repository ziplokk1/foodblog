# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class ScraperPipeline(object):
    def process_item(self, item, spider):
        text = item['post_content'].strip()
        if not text:
            raise DropItem
        item['post_content'] = text
        return item
