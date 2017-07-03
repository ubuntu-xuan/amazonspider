# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


# class AmazonPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('qa.jl', 'wb', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         question = []
#         for questions in item['question']:
#             question.append(questions.strip().replace('\n',''))
#         item['question'] = question
#         #
#         #
#         #
#         # line = json.dumps(dict(item),ensure_ascii=False) + "\n"
#         # self.file.write(line)
#         print '-------++++++++++'
#         print item
#
#
#         return item


#保存数据到mongodb
import pymongo

class AmazonPipelineByMongo(object):
    collection_name = 'description'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_SERVER'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        # question = []
        # for questions in item['question']:
        #     question.append(questions.strip().replace('\n',''))
        #     item['question'] = question
        #
        # answer = []
        # for answers in item['answer']:
        #     answer.append(answers.strip().replace('\n',''))
        #     item['answer'] = answer

        productname = []
        for productnames in item['productname']:
            productname.append(productnames.strip().replace('\n',''))
            item['productname'] = productname



        description = []
        for descriptions in item['description']:
            description.append(descriptions.strip().replace('\n','').replace('\t',''))
            item['description'] = description

        self.db[self.collection_name].insert(dict(item))
        return item