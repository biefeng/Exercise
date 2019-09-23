# -*- coding:utf-8 -*-
# filename : catch_mingchaonaxieshi


import requests

param = "?140022266897614x1565697514x140022273028274-61756bbb2253b313200f47bc127aba"
url = "http://177j.tt56w.com:8000/历史军事/明朝那些事儿_王更新/明朝那些事儿_"
# url = url + "001" + ".mp3" + param
# response = requests.get(
#     url=url,
#     headers={"Range": "bytes=0-1"})
# h = response.headers['Content-Range']
# h = h[h.rfind('/') + 1:]
# print(h)
# index = 1


def m(i):
    s = str(i)
    if s.__len__() == 1:
        s = "00" + s
    elif s.__len__() == 2:
        s = "0" + s
    return s


for index in range(267,268):
    with open("d:/Download/audio/" + "明朝那些事儿_" + str(index + 1) + ".mp3","wb") as download:
        tmp = url + m(index + 1) + ".mp3" + param
        requests_get = requests.get(tmp, headers={"Range": "bytes=0-1"})
        h = requests_get.headers['Content-Range']
        h = h[h.rfind('/') + 1:]
        range="bytes=0-" + str(h)
        content = requests.get(tmp, headers={"Range": range})
        print("downloading index: "+str(index+1))
        download.write(bytes(content.content))

