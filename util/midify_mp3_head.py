# -*- coding: utf-8 -*-

import eyed3
import os

for root, dirs, files in os.walk("d:/Download/audio"):
    load = eyed3.load(root+"/"+files[1])
    print(load.tag)
