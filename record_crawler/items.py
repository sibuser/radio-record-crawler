import scrapy


class Mp3FilesItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field