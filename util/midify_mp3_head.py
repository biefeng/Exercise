# -*- coding: utf-8 -*-

from mp3_tagger import MP3File
import os
import re

p = re.compile("[0-9]+")

for root, dirs, files in os.walk("D:\\Download\\audio\\诛仙"):
    for file in files:
        file_name = root + "/" + file
        mp_file = MP3File(file_name)
        mp_file.album = 'audio'
        mp_file.artist = 'BieFeNg'
        file = file[:file.index(".mp3")]
        mp_file.song = str(bytes(file, encoding="gbk"), encoding="ISO-8859-1")
        mp_file.save()
