import os                           #METTE IN ORDINE FOTO IN BASE AL NOME PER TELEFONO SAMSUNG
import shutil

import PIL
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

import sys
import datetime
from datetime import datetime
import admin
import time

from os import listdir
from os.path import isfile, join

from win32_setctime import setctime


import win32file, win32con

pat="C:\\Users\\marco\\Desktop\\o"
mylist = os.listdir(pat)


for i in mylist:

    if i !="test.py" and i !="sbagliate" and i!="boh" and i!="video" and i!="change.py" and i!="change":


        import win32api
        print(i[0:19])
        date=datetime.strptime(i[0:19],'%Y_%m_%d %H_%M_%S')
        modTime = time.mktime(date.timetuple())
        os.utime(pat+'\\'+i, (modTime, modTime))
        setctime(pat+'\\'+i, modTime)
