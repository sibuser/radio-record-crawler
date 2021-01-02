from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from record_crawler.spiders.history_record import HistoryRecordSpider


process = CrawlerProcess(get_project_settings())
process.crawl(HistoryRecordSpider)
process.start()