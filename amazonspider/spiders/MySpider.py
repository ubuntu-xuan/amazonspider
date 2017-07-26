# -*- coding:utf-8 -*-
from scrapy.loader import ItemLoader, Identity

__author__ = 'xuan'

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
# from amazonspider.items import AmazonItem
from amazonspider.items import AmazonItem
from amazonspider.pipelines import *

import sys
from scrapy.crawler import  CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner




reload(sys)
sys.setdefaultencoding('utf8')

class AmazomSpider(CrawlSpider):
    name = 'amazonspider'

    allowed_domains = ["www.amazon.com"]
    start_urls = [sys.argv[1]]
    '''
Rule(LinkExtractor(allow=r'https://www.amazon.com/ask/questions/asin/(\w+.*)/(\d+.*)/ref=ask_ql_psf_ql_hza',)),
        Rule(LinkExtractor(allow=r'https://www.amazon.com/(\w+.*)/forum/(\w+.*)/(\w+.*)/(\d+.*)/ref=cm_cd_al_psf_al_pg(\d+.*)\?_encoding=UTF8&asin=(\w+.*)',)), #注意这里的问号要用转义符)

        Rule(LinkExtractor(allow=r'https://www.amazon.com/forum/-/(\w+.*)/ref=ask_ql_ql_al_hza\?asin=(\w+.*)',), #注意这里的问号要用转义符
             callback='parse_item'),


        productname = response.xpath("//h1[@id='title']/span[@id='productTitle']/text()").extract()
        description = response.xpath("//div[@id='featurebullets_feature_div']/div[@id='feature-bullets']/ul[@class='a-unordered-list a-vertical a-spacing-none']/li/span[@class='a-list-item']/text()").extract()


        item['productname'] = productname
        item['description'] = description

    '''

    rules = [
	    Rule(LinkExtractor(allow=r'https://www.amazon.com/(\w+.*)/product-reviews/(\w+.*)/ref=cm_cr_arp_d_show_all\?ie=UTF8&reviewerType=all_reviews&pageNumber=(\d+.*)',),callback='parse_item',follow=True),
	]


    def parse(self,response):
        item = AmazonItem()

        rating = response.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@class='a-link-normal']/i[contains(@data-hook,'review-star-rating')]/span[@class='a-icon-alt']/text()").extract_first()
        author = response.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-author']/a[@data-hook='review-author']/text()").extract_first()
        body = response.xpath("normalize-space(div[@class='a-section celwidget']/div[@class='a-row review-data']/span[@data-hook='review-body']/text())").extract_first()


        item['rating'] = rating
        item['author'] = author
        item['body'] = body
        yield item

if __name__ == '__main__':
    if len(sys.argv) == 2:
        settings = get_project_settings()
        process = CrawlerProcess(settings=settings)

        process.crawl(AmazomSpider)
        process.start()
    else:
        print "[-] For example[python -m python -m amazonspider.spiders.MySpider 'url']"
