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

        if url is not None:
            #先删除数据库记录
            #创建连接
            client = MongoClient('localhost',27017)
            #连接数据库
            db = client.scrapy

            collection = db.myspider
            collection.remove({})

            commands.getstatusoutput("cd %s"%os.getcwd())
            run = commands.getstatusoutput("python -m amazonspider.spiders.MySpider %s"%(url))

            description = collection.find_one()["description"]
            productname = collection.find_one()["productname"]

            jsonData = []

            result = {}
            result['description'] = description
            result['productname'] = productname

            jsonData.append(result)


            return simplejson.dumps(result)

    
    return render_template('index/spider.html')




