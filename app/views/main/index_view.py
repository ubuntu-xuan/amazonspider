# -*- coding:utf-8 -*-
__author__ = 'xuan'

from flask import render_template,request,current_app,session,redirect,url_for,send_from_directory,flash
from . import  main
from  manage import  db
from  manage import app
import commands
import sys,json
import simplejson
from flask.ext.login import login_required, current_user, login_user, logout_user
from more_itertools import chunked
import os
import difflib
from config import config
from lib.upload_file import uploadfile
from werkzeug.utils import secure_filename
from datetime import datetime
import time
import requests
from lxml import html

import  pymongo
from  pymongo import MongoClient

reload(sys)
sys.setdefaultencoding('utf8')


@main.route('/spider',methods=['GET','POST'])
@login_required
def spider():
    if request.method == 'POST':

        data = request.form.get('data', '')
        # print "++++++--++",json.loads(data)["number"]

        url = json.loads(data)["URL"]
        #print('****************************')
        #print(url)

        if url is not None:
            #先删除数据库记录
            #创建连接

            print(u'正在爬取中,请等候......')

            flash(u'正在爬取中,请等候......')

            client = MongoClient('localhost',27017)
            #连接数据库
            db = client.myspider

            collection_description = db.myspider_description
            collection_description.remove({})

            collection_reviews = db.myspider_reviews
            collection_reviews.remove({})

            collection_qa = db.myspider_qa
            collection_qa.remove({})


            run = commands.getstatusoutput("python -m amazon.spiders.amazonspider %s"%(url))
            #print(run)

            print(os.getcwd())

            mongoexport_reviews = commands.getstatusoutput("mongoexport -d myspider -c myspider_reviews --csv -f title,rating,author,date,body -o %s/app/static/csv/reviews.csv"%os.getcwd())

            mongoexport_qa = commands.getstatusoutput("mongoexport -d myspider -c myspider_qa --csv -f question,answer -o %s/app/static/csv/qa.csv"%os.getcwd())


            query_description = collection_description.find({},{"description":1,"_id":0})
            print("query_description")
            print(query_description)

            query_productname = collection_description.find({},{"productname":1,"_id":0})

            description = ''
            if query_description is not None:
                for info in query_description:
                    print(info)
                    for i in info["description"]:
                        description += i

            productname = ''
            if query_productname is not None:
                for info in query_productname:
                    for i in info["productname"]:
                        productname += i



            jsonData = []

            result = {}
            result['description'] = description
            result['productname'] = productname

            jsonData.append(result)


            return simplejson.dumps(result)

    
    return render_template('index/spider.html')




