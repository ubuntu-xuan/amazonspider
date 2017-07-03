# -*- coding:utf-8 -*-
__author__ = 'xuan'


import  re

link = 'https://www.amazonspider.com/forum/-/TxSQOV7HIYMHFT/ref=ask_ql_ql_al_hza?asin=B012ZPKNFE'
links = 'http://www.discuz.net/thread-3778501-23-1.html'
links3= 'https://www.amazonspider.com/ask/questions/asin/B0076OUOL8/2/ref=ask_dp_iaw_ql_hza?isAnswered=true#question-Tx20MO15Q5LEYYM'

link_regex1=r'http://www.discuz.net/thread-(\d+)-(\d+)-1\.html'
result = re.match(link_regex1, links)

link_regex2=r'https://www.amazonspider.com/forum/-/(\w+.*)/ref=ask_ql_ql_al_hza\?asin=(\w+.*)'
result2 = re.search(link_regex2, link)

link_regex3 = r'https://www.amazonspider.com/ask/questions/asin/(\w+.*)/(\d+.*)/ref=ask_dp_iaw_ql_hza\?isAnswered=true#question-(\w+.*)'
result3 = re.search(link_regex3,links3)


print(result.group())
print(result2.group())
print(result3.group())



