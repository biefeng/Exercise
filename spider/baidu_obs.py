# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/06/15 23:02
# file_name : baidu_obs.py

import base64
import hashlib
import logging
import os, io

from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.bos.bos_client import BosClient

_bos_host = "genious.cdn.bcebos.com"
_access_key_id = "9a137e5669e04e1ca994adbe435d644c"
_secret_access_key = "9e89feeb688345cda556992a1065a274"

logger = logging.getLogger('baidubce.http.bce_http_client')

config = BceClientConfiguration(credentials=BceCredentials(_access_key_id, _secret_access_key), endpoint=_bos_host)

bos_client = BosClient(config)

GENIOUS_BUCKET = 'genious'


def md5_obj(fp):
    buf_size = 8192
    md5 = hashlib.md5()
    while True:
        bytes_to_read = buf_size
        buf = fp.read(bytes_to_read)
        if not buf:
            break
        md5.update(buf)
    content_md5 = base64.standard_b64encode(md5.digest())
    return content_md5


if __name__ == '__main__':
    fp = open("E:\workspace\pycharm\Exercise\spider\chrome_plugin\Clear Cache.crx", 'rb')
    getsize = os.path.getsize("E:\workspace\pycharm\Exercise\spider\chrome_plugin\Clear Cache.crx")
    bs = bytearray(getsize)
    readinto = fp.readinto(bs)
    print(getsize)
    bos_client.put_object("genious", "chrome/crx/11.crx", io.BytesIO(bs), getsize, md5_obj("E:\workspace\pycharm\Exercise\spider\chrome_plugin\Clear Cache.crx"))
