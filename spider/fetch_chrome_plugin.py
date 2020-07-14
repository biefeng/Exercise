# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/06/14 10:48
# file_name : fetch_chrome_plugin.py

import csv
import json
import datetime
import pymysql
import requests

login_info = {
    "login": "biefeng6@gmail.com",
    "t": "AHUv8HGOzaKV-HYwj4U1lNAXr3McNfUGbw:1592218704450"
}

categories = ['collection/editors_picks_extensions', 'recommended_extensions']


def fetch_plugin_info_into_file():
    category = categories[0]
    url = "https://chrome.google.com/webstore/ajax/item?hl=zh-CN&gl=SG&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma%2Cigb%2Cpot%2Cevt&count=25&token=0%406610547&marquee=true&category={0}&sortBy=0&container=CHROME&_reqid=1575722&rt=j".format(category)

    payload = "login=biefeng6%40gmail.com&t=AHUv8HGVbwkC64QjdORSraG9H2eDGPVPjw%3A1592103479503&"
    headers = {
        'authority': 'chrome.google.com',
        'x-same-domain': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept': '*/*',
        'origin': 'https://chrome.google.com',
        'x-client-data': 'CI62yQEIpbbJAQjEtskBCKmdygEYm77KAQ==',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://chrome.google.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'ANID=AHWqTUmhsPFfP5pos-5AqVvBZugFEgrv7YNCQp5C7Jzw9TYscKQTzUmn2EPpQC0D; SID=xwfxZdPhUjPqWljFqcHP5kZ4Mxka2cSG5cfcJajlt9UKj0gOKyvptdgSiIjGKy3o76ZP6g.; __Secure-3PSID=xwfxZdPhUjPqWljFqcHP5kZ4Mxka2cSG5cfcJajlt9UKj0gO1XuRH06_D4sLDu8Ls62hyw.; HSID=AXJ-3nljB9GXLEu6W; SSID=AeBSiWKGcAZ8adS51; APISID=ZeTbkaSeQFhQ-_ag/AloYOr7XCpCE5nLU-; SAPISID=-7I1uSrR_xJanry2/ATxMaK0_xiB60pHUV; __Secure-HSID=AXJ-3nljB9GXLEu6W; __Secure-SSID=AeBSiWKGcAZ8adS51; __Secure-APISID=ZeTbkaSeQFhQ-_ag/AloYOr7XCpCE5nLU-; __Secure-3PAPISID=-7I1uSrR_xJanry2/ATxMaK0_xiB60pHUV; __utmc=73091649; SEARCH_SAMESITE=CgQI-I8B; NID=204=Jn1zTKpZeKtokIIwKuBZ43beDP6UqawXZaKjAfImLjoQIaA3PNkJDo58iPZMxAmlBcdv4ltScjbvlnKUw-KUejBQWeqZBEwJzj1ldm2vA6ilia_64-iE8Wu-azw8P7JOsUP-iC_WNKBTdkcVp-IETKCdfcJwSzLDFABw89an6Dp_ScoETxEphv68zAZHg8XKj9ymhuYFPlLVfWF4zdjYw3Vv6Z0T_5KjsI40kINO; 1P_JAR=2020-6-12-14; __utma=73091649.1825346260.1591807403.1591883790.1592102335.4; __utmz=73091649.1592102335.4.3.utmcsr=chrome-ntp-icon|utmccn=(not%20set)|utmcmd=(not%20set); __utmt=1; __utmb=73091649.119.9.1592103483262; SIDCC=AJi4QfFovZFo4oGtEi_A6Tt-ggYB-eGPEiwZSH7ZNrbrqQeohCWrFmr1AS1omvY7kuQIWBwQ5do; SIDCC=AJi4QfHpZ-9FtctIowwPFLe5mySnzgBNx1jb39UNjq0Sro5OWC29nocxKtbp7XyAt0SRhR_NAiY'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    data_str = response.text.encode("utf-8").replace(b"\n", b"")[4:].decode("utf-8").replace("null", "\"null\"")
    # print(dataStr)
    data = (json.loads(data_str))
    with open('chrome_plugin.csv', encoding='utf-8', mode="w") as sql_file:
        writer = csv.DictWriter(sql_file, fieldnames=['name', 'short_desc', 'description'], delimiter=r" ")
        writer.writeheader()
        for i in data[0][1][1]:
            print(i[0] + ": " + i[1] + " " + i[6])
            detail_url = "https://chrome.google.com/webstore/ajax/detail?hl=zh-CN&gl=SG&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&id={0}&container=CHROME&_reqid=177793&rt=j".format(
                i[0])
            # print(detail_url)
            detail_res = requests.post(detail_url, data=payload, verify=False)
            detail = json.loads(detail_res.text[4:])
            # print(detail[0][1][1][1])
            plugin_data = {
                'name': i[1],
                'short_desc': i[6],
                'description': detail[0][1][1][1]
            }
            sql = "insert into chrome_plugin (name,short_desc,description) values ('{0}','{1}','{2}');".format(i[1], i[6], detail[0][1][1][1])
            writer.writerow(plugin_data)
            download_crx(i[0], i[1])
            # break


def insert_plugin_info_into_mysql():
    connect = pymysql.connect(host="106.13.83.252", user='root', db='blog_mini', passwd='Biefeng123!')
    cursor = connect.cursor()

    with open('chrome_plugin.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=' ')
        for row in reader:
            plugin_data = [
                row['name'],
                row['short_desc'],
                datetime.datetime.now(),
                datetime.datetime.now(),
                row['description']
            ]
            sql = "insert into chrome_plugin (name,short_desc,create_time,update_time,description) values (%s,%s,%s,%s,%s)"
            cursor.execute(sql, plugin_data)

    connect.commit()


def download_crx(id, name):
    url = "https://clients2.google.com/service/update2/crx?response=redirect&os=win&arch=x64&os_arch=x86_64&nacl_a" \
          "rch=x86-64&prod=chromecrx&prodchannel=&prodversion=83.0.4103.97&lang=zh-CN&acceptformat=crx3&x=id%3D{0}%26installsource%3Dondemand%26uc".format(
        id)
    s = requests.session()

    s.keep_alive = False
    payload = {}
    headers = {
        # 'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Client-Data': 'CI62yQEIpbbJAQjEtskBCKmdygEYm77KAQ==',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'ANID=AHWqTUmhsPFfP5pos-5AqVvBZugFEgrv7YNCQp5C7Jzw9TYscKQTzUmn2EPpQC0D; SID=xwfxZdPhUjPqWljFqcHP5kZ4Mxka2cSG5cfcJajlt9UKj0gOKyvptdgSiIjGKy3o76ZP6g.; __Secure-3PSID=xwfxZdPhUjPqWljFqcHP5kZ4Mxka2cSG5cfcJajlt9UKj0gO1XuRH06_D4sLDu8Ls62hyw.; HSID=AXJ-3nljB9GXLEu6W; SSID=AeBSiWKGcAZ8adS51; APISID=ZeTbkaSeQFhQ-_ag/AloYOr7XCpCE5nLU-; SAPISID=-7I1uSrR_xJanry2/ATxMaK0_xiB60pHUV; __Secure-HSID=AXJ-3nljB9GXLEu6W; __Secure-SSID=AeBSiWKGcAZ8adS51; __Secure-APISID=ZeTbkaSeQFhQ-_ag/AloYOr7XCpCE5nLU-; __Secure-3PAPISID=-7I1uSrR_xJanry2/ATxMaK0_xiB60pHUV; SEARCH_SAMESITE=CgQI-I8B; NID=204=aO8ahavbzR4kfQLxTqCCBheqrJi6alg1CvwjC0qxSP0gY7yrAggb6R_fSuHTSRj7RxxopR2720qQhTjH3eiceWR_Q51Okhp3WD7tDgY_oLFWgxUSlu_ujM310s3TfBJeehnBuSX0qed2P5h914tBdG-W65lgwb_Vl33IJz42y5RlL25TGO4ViIyz-JnLmkoRAu-rAbJ9zl3Oj3TEIfdl-sv20M1LvGqcy4Jmp4GG; 1P_JAR=2020-6-15-7; SIDCC=AJi4QfFwFtK3YK1W4ZA2-MHUimwWsLBePsEJ4ytg_m2LxCXG7RfjFuIm3iinCGJeFUes-ixHI3M; SIDCC=AJi4QfGiX-IvK-ndyoj6oc-acrm030PE1PwQn_zdRu_8TYB5RKXSul_uR17kefmO3ShO8TJID3E'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    with open("chrome_plugin/" + name + ".crx", mode='wb') as crx_file:
        crx_file.write(response.content)
        crx_file.flush()


def upload_to_baidu_obs(fn, bs):
    bi = io.BytesIO(bs)
    bos_client.put_object(GENIOUS_BUCKET, "chrome/crx/" + fn, bi, len(bs), md5_obj(bi))


if __name__ == '__main__':
    fetch_plugin_info_into_file()
