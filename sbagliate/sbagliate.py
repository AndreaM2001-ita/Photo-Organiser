import os
import shutil

import PIL
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

from os import listdir
from os.path import isfile, join

pat="C:\\Users\\marco\\Desktop\\imm\\sbagliate"
mylist = os.listdir(pat)
r=0
s=0
for i in mylist:
    if not i=="sbagliate.py":
        if i[0:8]=="Snapchat":
            import os.path, time
            k=os.path.getmtime(i)
            g=time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(k))
            try:
                os.rename(pat+'\\'+i, pat+'\\'+g+ '.jpg')
            except FileExistsError:
                os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(r)+')'+ '.jpg')
                r=r+1
