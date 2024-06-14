import os
import shutil

import PIL
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

from os import listdir
from os.path import isfile, join

pat="C:\\Users\\marco\\Desktop\\imm\\video"
mylist = os.listdir(pat)

s=0
for i in mylist:
    if not i=="video.py":

        if i[0:4]=="VID-" or i[0:4]=="VID_":
            k=i[4:12]
        else:
            k=i
        g=k[0:4]+"_"+k[4:6]+"_"+k[6:8]
        print(g)
        try:
            os.rename(pat+'\\'+i, pat+'\\'+g+ '.mp4')
        except FileExistsError:
            os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(s)+')'+ '.mp4')
            s=s+1
#
