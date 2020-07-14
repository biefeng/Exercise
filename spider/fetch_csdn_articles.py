# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/05/27 0:18
# file_name : fetch_csdn_articles.py

import html
from datetime import datetime

import pymysql
import requests
from bs4 import BeautifulSoup


def correct_title(title):
    error_set = ['/', '\\', ':', '*', '?', '"', '|', '<', '>']
    result = ""
    for c in title:
        if c in error_set:
            title = title.replace(c, '')
    return title


connect = pymysql.connect(host="106.13.83.252", port=3306, user='root', password='Biefeng123!', database='blog_mini')
cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

for i in range(100):
    article_list_url = "https://www.csdn.net/api/articles?type=new&category=java"

    article_detail_url = "https://blog.csdn.net/qq_40242512/article/details/106330430?utm_medium=distribute.pc_category.none-task-blog-hot-2.nonecase&depth_1-utm_source=distribute.pc_category.none-task-blog-hot-2.nonecase&request_id="

    article_list_res = requests.post(article_list_url).json()

    if ("articles" in article_list_res.keys()):
        articles = article_list_res['articles']
        for article in articles:
            try:
                url_ = article['url']
                # print(url_)
                article_detail_url = url_ + "?utm_medium=distribute.pc_category.none-task-blog-hot-2.nonecase&depth_1-utm_source=distribute.pc_category.none-task-blog-hot-2.nonecase&request_id="
                detail_res = requests.get(article_detail_url)
                article_main = BeautifulSoup(detail_res.text, 'html.parser').main
                title = article_main.find(attrs={"class": "title-article"}).text
                title = correct_title(title)
                content = str(article_main.article)
                content = html.escape(content)

                # content = content.replace('"', '&#34;').replace("'",
                #                                                 "&#39")  # .replace('&', '&#38;').replace("<","&#60;").replace(">","&#62;")
                summary = article_main.article.text[:50]
                # sql = "insert into articles (title,content,summary) values(" + "'" + title + "'," + "'" + content + "');"
                sql = "insert into articles (title,content,summary,ref_url,create_time,update_time,num_of_view,articleType_id,source_id)" \
                      " values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(title, content, summary,
                                                                                               url_, datetime.now(),
                                                                                               datetime.now(), 1, 1, 1)

                cursor.execute(sql)
            except Exception as e:
                print(e)
            finally:
                connect.commit()

            # with open(title, 'w', encoding='utf-8') as article_file:
            #     article_file.write(str(article_main.article))
connect.close()
