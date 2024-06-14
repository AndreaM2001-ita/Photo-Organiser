import os
import shutil

import PIL
import piexif
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

from os import listdir
from os.path import isfile, join

pat="C:\\Users\\marco\\Desktop\\imm\\boh"
mylist = os.listdir(pat)
r=0
s=10

for i in mylist:

    if not i=="boh.py" and i !="emm":
        print(i)

        g='2016_00_00 00_00_'

        try:
            os.rename(pat+'\\'+i, pat+'\\'+g+str(s)+'.jpg')
        except FileExistsError:
            os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(r)+')'+ '.jpg')
            r=r+1
        s=s+1
