# -*- coding:utf-8 -*-
from scrapy.loader import ItemLoader, Identity

__author__ = 'xuan'

from scrapy.spiders import CrawlSpider,Rule
from amazonspider.items import AmazonItem
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class AmazomSpider(CrawlSpider):
    name = 'amazonspider'

    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/InnoGear-Security-Lighting-Activated-Detector/dp/B01MR18DLU/"
                  "ref=sr_1_18?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-18&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/Mpow-Powered-Security-Wireless-Waterproof/dp/B015CCL1V2/"
                  "ref=sr_1_16?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-16&keywords=Solar+Motion+Sensor+Wall+Lights ",
                  "https://www.amazon.com/Mulcolor-Outdoor-Wireless-Security-Intelligent/dp/B06VT31CFZ/ref=sr_1_15?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-15&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/Mpow-Lights-Waterproof-Outdoor-Lighting/dp/B01D1H89DI/ref=sr_1_9?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-9&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/Iextreme-Waterproof-Wireless-Security-Driveway/dp/B071L8TW9K/ref=sr_1_8?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-8&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/Litom-Bright-Outdoor-Motion-Sensor/dp/B01JS285JS/ref=sr_1_7?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-7&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/URPOWER-Wireless-Waterproof-Exterior-Security/dp/B012ZDE54G/ref=sr_1_5?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-5&keywords=Solar+Motion+Sensor+Wall+Lights",
                  "https://www.amazon.com/BAXIA-TECHNOLOGY-Outdoor-Waterproof-Security/dp/B01HCQL17U/ref=sr_1_4?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-4&keywords=Solar+Motion+Sensor+Wall+Lights"







                  ]

    #QA
    # rules = [
    #     Rule(LinkExtractor(allow=r'https://www.amazonspider.com/ask/questions/asin/(\w+.*)/(\d+.*)/ref=ask_ql_psf_ql_hza',)),
    #     Rule(LinkExtractor(allow=r'https://www.amazonspider.com/(\w+.*)/forum/(\w+.*)/(\w+.*)/(\d+.*)/ref=cm_cd_al_psf_al_pg(\d+.*)\?_encoding=UTF8&asin=(\w+.*)',)), #注意这里的问号要用转义符)
    #
    #     Rule(LinkExtractor(allow=r'https://www.amazonspider.com/forum/-/(\w+.*)/ref=ask_ql_ql_al_hza\?asin=(\w+.*)',), #注意这里的问号要用转义符
    #          callback='parse_item',follow = True),
    #
    #     # Rule(LinkExtractor(allow=r'InnoGear-Security-Lighting-Activated-Detector/dp/(\w+.*)/ref=sr_1_18\?s=lawn-garden&ie=UTF8&qid=1499061852&sr=1-18&keywords=Solar+Motion+Sensor+Wall+Lights',), #注意这里的问号要用转义符
    #     #      callback='parse_item2',follow = True),
    #
    # ]



    # def parse_item(self,response):
    #     item = AmazonItem()
    #
    #     question = response.xpath("normalize-space(//div[@class='cdQuestionText']/text())").extract_first()
    #     answer = response.xpath("//div[@class='cdMessageInfo']/span[contains(@id,'cdPostContentBox_')]/text()").extract()
    #
    #     #rating = response.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@class='a-link-normal']/i[contains(@data-hook,'review-star-rating')]/span[@class='a-icon-alt']/text()").extract_first()
    #     # author = response.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-author']/a[@data-hook='review-author']/text()").extract_first()
    #     # date = response.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-date']/text()").extract_first()
    #     # body = response.xpath("normalize-space(div[@class='a-section celwidget']/div[@class='a-row review-data']/span[@data-hook='review-body']/text())").extract_first()
    #
    #
    #     description = response.xpath("//div[@id='productDescription']/p/text()").extract()
    #     item['description'] = description
    #
    #     item['question'] = question
    #     item['answer'] = answer
    #
    #
    #     # item['rating'] = rating
    #     # item['author'] = author
    #     # item['date'] = date
    #     # item['body'] = body
    #
    #     yield item

    def parse(self,response):
        item = AmazonItem()

        productname = response.xpath("//h1[@id='title']/span[@id='productTitle']/text()").extract()
        description = response.xpath("//div[@id='featurebullets_feature_div']/div[@id='feature-bullets']/ul[@class='a-unordered-list a-vertical a-spacing-none']/li/span[@class='a-list-item']/text()").extract()
        # description2 = response.xpath("//div[@id='productDescription_feature_div']/div[@id='productDescription']/p/text()").extract()


        item['productname'] = productname
        item['description'] = description

        yield item
