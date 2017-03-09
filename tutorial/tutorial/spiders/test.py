# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-03-07
    
"""
import json
import scrapy
from bs4 import BeautifulSoup


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["qiushibaike.com"]
    page = 1
    start_urls = [
        'http://www.qiushibaike.com/'
    ]

    def parse(self, response):
        # filename = 'qsbk.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        soup = BeautifulSoup(response.body)
        data = list()
        args = dict()
        args['page'] = TestSpider.page

        authors = soup.find_all(class_="article block untagged mb15")
        for authou in authors:
            main = authou.find(class_="content")
            if main.span.string is None:
                continue
            args['名字'] = authou.h2.string
            print '名字：', authou.h2.string
            args['内容'] = main.span.string
            print '内容：', main.span.string
            number = authou.find(class_="number")
            args['点赞数'] = number.string
            data.append(args)
            print '点赞数：', number.string
            print ''
        data = json.dumps(data).decode('unicode-escape')
        print data
        with open('data.txt', 'a') as f:
            f.write('\n'+data.encode('utf-8'))
        pages = soup.find(class_="pagination")
        next_page = pages.find(class_="next").parent.get('href')
        next_full_url = response.urljoin(next_page)
        TestSpider.page += 1
        if TestSpider.page == 3:
            yield None
        else:
            yield scrapy.Request(next_full_url, callback=self.parse)
