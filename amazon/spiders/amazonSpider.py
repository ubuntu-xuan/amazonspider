# -*- coding:utf-8 -*-
from scrapy.loader import ItemLoader, Identity

__author__ = 'xuan'

from scrapy.spiders import CrawlSpider,Rule
from amazon.items import AmazonItem
from scrapy.selector import Selector
from scrapy.http import Request
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class AmazomSpider(CrawlSpider):
    name = 'amazon'

    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/Mae-Womens-Seamless-Cheekini-Panty/product-reviews/B01MQM0813/ref=cm_cr_arp_d_show_all?ie=UTF8&reviewerType=all_reviews&pageNumber=1"]


    def parse(self,response):
        review_list = response.xpath("//div[@data-hook='review']")


        '''这里多加一个//div[@class='a-section askTeaserQuestions']是因为'a-fixed-left-grid a-spacing-base'还有一个'a-fixed-left-grid a-spacing-base'标签'''
        #qa_list = response.xpath("//div[@class='a-section askTeaserQuestions']/div[@class='a-fixed-left-grid a-spacing-base']")

        for info in review_list:

            item = AmazonItem()

            rating = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@class='a-link-normal']/i[contains(@data-hook,'review-star-rating')]/span[@class='a-icon-alt']/text()").extract_first()
            title = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/a[@data-hook='review-title']/text()").extract_first()
            author = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-author']/a[@data-hook='review-author']/text()").extract_first()
            date = info.xpath("div[@class='a-section celwidget']/div[@class='a-row']/span[@data-hook='review-date']/text()").extract_first()
            body = info.xpath("normalize-space(div[@class='a-section celwidget']/div[@class='a-row review-data']/span[@data-hook='review-body']/text())").extract_first()

            item['rating'] = rating
            item['title'] = title
            item['author'] = author
            item['date'] = date
            item['body'] = body

            # '''QA'''
            # '''当要在pipelines中处理items时，用extract，否则用extract_first()专直接把文字取出来'''
            # question = info.xpath("div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/div[@class='a-fixed-left-grid a-spacing-small']/div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/a[@class='a-link-normal']/text()").extract()
            # answer = info.xpath("div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/div[@class='a-fixed-left-grid a-spacing-base']/div[@class='a-fixed-left-grid-inner']/div[@class='a-fixed-left-grid-col a-col-right']/span/text()").extract()
            #
            #
            # item['question'] = question
            # item['answer'] = answer




            yield item

            nextLink = response.xpath('//li[@class="a-last"]/a/@href').extract()
            print ('pages %s' % nextLink)


            #有下一页的链接继续,没有下一页的连接时停止
            if nextLink:
                nextLink = nextLink[0]
                #print nextLink
                yield Request('https://www.amazon.com' + nextLink,callback=self.parse)