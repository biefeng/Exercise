# -*- coding:utf-8 -*-
# filename : map_prop_editor

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

audiofile = MP3File(path="D:\\Download\\audio\\song.mp3")
alb = audiofile.album
print(alb)
audiofile.album = 'some title'
audiofile.save()
print(alb)
