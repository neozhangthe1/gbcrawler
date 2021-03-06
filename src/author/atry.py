from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from author.spiders.titlespider import Titlespider
from scrapy.utils.project import get_project_settings
import time

while True:
	spider = Titlespider()
	settings = get_project_settings()
	crawler = Crawler(settings)
	crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
	crawler.configure()
	crawler.crawl(spider)
	crawler.start()
	log.start()
	reactor.run()
	time.sleep(60)