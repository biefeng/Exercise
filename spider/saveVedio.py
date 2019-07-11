import requests

url_prefix = r"http://v-cc.dushu.io/video/full/87de06c56944d9415cd40650ff91a1a0/87de06c56944d9415cd40650ff91a1a0.mp4_"
url_suffix = ".ts"
headers = {
    'Cookie': 'grwng_uid=e7e51c80-ead6-43bb-9744-7531778d6c73; UM_distinctid=16be039d03e8aa-0f0e963eb0f589-621c740a-4a640-16be039d03f633; gr_user_id=ebc67f00-d109-4c29-80b0-7d631382debf',
    'X-Playback-Session-Id': 'E771E40D-D0D1-42EE-95D6-7665D0C52496',
    'Connection': 'keep-alive',
    'Host': 'v-cc.dushu.io'
}
with open("111111.mp4", 'wb') as saved:
    for i in range(381):
        url = url_prefix + str(i + 1) + url_suffix
        response = requests.get(url=url, headers=headers)
        saved.write(bytes(response.content))
        print("请求到第" + str(i) + "个")
