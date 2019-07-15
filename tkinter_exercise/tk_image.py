# -*- coding: utf-8 -*-
__author__ = '33504'

from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import requests

win = Tk()
win.geometry("300x300+20+20")
response = requests.get(
	"http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLejPu6rznotfZKyGSNzvhs29EC1yAXZAZe9XdOuWQU6tDxS6G5PMzn2BNPNq1RH3icgvrepCeELdg/132")
image = Image.open(r'avatar.ppm')
image = image.resize((40, 40), Image.ANTIALIAS)
image.save(r"avatar.ppm")
avatar = PhotoImage(file=r'images\avatar.ppm')
photo_image = PhotoImage(file=r'images\avatar.ppm')
label = Label(win, image=photo_image)
label.pack()

win.mainloop()
