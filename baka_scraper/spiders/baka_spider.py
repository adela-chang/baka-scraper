# -*- coding: utf-8 -*-
import scrapy
import re

class BakaSpider(scrapy.Spider):
    name = 'baka_spider'
    download_delay = 0.5
    allowed_domains = ['www.mangaupdates.com']
    start_urls = ['https://www.mangaupdates.com/publishers.html?id=279']

    def parse(self, response):
        urls = response.css('a::attr(href)').getall()
        for url in urls:
            if "series.html?id" in url:
                yield response.follow(url, callback=self.parse_series)
    
    def parse_series(self, response):
        sectiontitles = response.xpath("//div[contains(@class,'sCat')]/b/text()").extract()
        sectioncontent = response.xpath("//div[contains(@class,'sCat')]/following-sibling::div[contains(@class,'sContent')]").extract()
        dict = {'title': response.css('.tabletitle::text').get() }
        for title, content in zip(sectiontitles, sectioncontent):
            sanitized = re.sub('<[^<]+?>', '', content)
            dict[title] = sanitized
        yield dict
