# -*- coding: utf-8 -*-
__author__ = '33504'

import requests

if __name__=='__main__':
	url = "http://gateway-api.dushu.io/search-orchestration-system/search/v100/searchUnited"

	payload = {"keyword":"第三","appId":"2002"}
	headers = {
		'Host': "gateway-api.dushu.io",
		'Accept': "*/*",
		'X-DUSHU-APP-VER': "3.9.46",
		'X-DUSHU-APP-PLT': "1",
		'Accept-Language': "en-CN;q=1, zh-Hans-CN;q=0.9, zh-Hant-CN;q=0.8",
		'X-DUSHU-APP-MUID': "A2E139A0-FDA6-49F4-A40B-A9A8E2CF049F",
		'Accept-Encoding': "br, gzip, deflate",
		'Content-Type': "application/json; charset=utf-8",
		'Content-Length': "35",
		'User-Agent': "bookclub/3.9.46 (iPhone; iOS 12.1.4; Scale/3.00)",
		'Connection': "keep-alive",
		'X-DUSHU-APP-SYSVER': "Version 12.1.4 (Build 16D57)",
		'X-DUSHU-APP-DEVID': "FD797288-5821-4A8B-9C21-187365BF8996",
		'X-DUSHU-APP-DEVTOKEN': "d870663f9e3d09db02a987d58050b108db2cc0246f83144cbc19a82454fc4b48",
		'Cookie': "grwng_uid=e7e51c80-ead6-43bb-9744-7531778d6c73; UM_distinctid=16be039d03e8aa-0f0e963eb0f589-621c740a-4a640-16be039d03f633; gr_user_id=ebc67f00-d109-4c29-80b0-7d631382debf",
		'cache-control': "no-cache",
		'Postman-Token': "bd9c0a33-b599-45b6-8a35-696b2e56480f"
	}

	response = requests.request("POST", url, json=payload, headers=headers)
	print(response.json())