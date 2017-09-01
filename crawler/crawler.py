#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy

class InfoSpider(scrapy.Spider):
    name = 'infospider'

    start_urls = ['https://bj.lianjia.com/ershoufang/']
    
    def parse(self, response):
        for content in response.css('div.leftContent ul.sellListContent div.title'):
            yield {'title': content.css('a::text').extract_first(), 
                    'house_id': content.css('a::attr(data-housecode)').extract_first()}
