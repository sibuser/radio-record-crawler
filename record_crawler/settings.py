BOT_NAME = 'record_crawler'

SPIDER_MODULES = ['record_crawler.spiders']
NEWSPIDER_MODULE = 'record_crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'record_crawler.pipelines.Mp3FilePipeline': 1}

FILES_STORE = '/media/dst'

CHANNELS = ['mdl', 'chil']
