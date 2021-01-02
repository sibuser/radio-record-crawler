import os
import re
import urllib.parse

import scrapy
from scrapy.spiders import CrawlSpider

from ..items import Mp3FilesItem
from ..settings import FILES_STORE, CHANNELS


class HistoryRecordSpider(CrawlSpider):
    name = "radiorecord"

    def start_requests(self):
        for channel in CHANNELS:
            yield scrapy.Request(url=f"http://history.radiorecord.ru/air/{channel}",
                                 callback=self.parse_channel)

    def parse_day(self, response):
        file_urls = []
        for song in response.css("a::attr(href)").getall()[2:]:
            channel = response.url.split('/')[-3]
            name = re.sub(r"\d\d:\d\d:\d\d - ", '', urllib.parse.unquote(song)).replace("\'", "")
            target = os.path.join(FILES_STORE, channel, name)
            if len(name) < 10:
                continue
            if os.path.isfile(target):
                continue

            self.log(f"Downloading {response.urljoin(song)}")
            file_urls.append(response.urljoin(song))
        item = Mp3FilesItem()
        item["file_urls"] = file_urls
        yield item

    def parse_channel(self, response):
        channel = response.url.split('/')[-2]
        for day in response.css("a::text").getall()[1:]:
            self.log(f'Parsing  {channel}/{day}')
            yield scrapy.Request(url=response.urljoin(day), callback=self.parse_day)
