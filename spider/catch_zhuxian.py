# -*- coding:utf-8 -*-
# filename : catch_zhuxian

import requests
from urllib import parse as parse
from json import JSONDecoder, JSONEncoder
import re

pattern = re.compile("http://t33.tingchina.com/yousheng/玄幻奇幻/诛仙_管恩亮/(?P<audio_name>.*?)\\?.*")
findall = pattern.search(
    'http://t33.tingchina.com/yousheng/玄幻奇幻/诛仙_管恩亮/第111章_玄火坛.mp3?key=762ce4593ed6d8bc3e803b327108905a_628790352')

# print(findall.group("dufio_name"))

url = "http://www.qktsw.com/qkmjs/tc.php"

headers_1 = {
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "df46e3fc-7fc3-4957-8be7-b712a53b320e,3286c797-b721-4102-a852-f56e98c899b6",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

headers_1 = {
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "df46e3fc-7fc3-4957-8be7-b712a53b320e,3286c797-b721-4102-a852-f56e98c899b6",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

headers_2 = {
    'Host': "t33.tingchina.com",
    'Connection': "keep-alive",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Accept-Encoding': "identity;q=1, *;q=0",
    'Accept': "*/*",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Range': "bytes=0-",
    'Cache-Control': "no-cache",
    'Postman-Token': "a6311dfb-28bd-4bf8-b4d8-da2cfeeb62c4,2f84ab46-093a-49c3-80f3-f505db39cc99",
    'cache-control': "no-cache"
}

phase_prefix = '玄幻奇幻/诛仙_管恩亮/第'
phase_suffix = '章_青云.mp3'


def m(i):
    s = str(i)
    if s.__len__() == 1:
        s = "00" + s
    elif s.__len__() == 2:
        s = "0" + s
    return s


for index in range(257):
    querystring = {}
    querystring['id'] = "yousheng/21056/" + str(index + 1)
    print(querystring)
    response = requests.request("GET", url, headers=headers_1, params=querystring)
    audio_url = response.json()
    search = pattern.search(audio_url['url'])
    file_name = "诛仙_" + str(index + 1) + ".mp3"
    if search is not None:
        file_name = "诛仙_" + search.group("audio_name")
    print(file_name)
    with open("d:/Download/audio/诛仙/" + file_name, "wb") as download:
        audio = requests.request('GET', audio_url['url'], headers=headers_2)
        print("downloading index: " + str(index + 1))
        download.write(bytes(audio.content))
