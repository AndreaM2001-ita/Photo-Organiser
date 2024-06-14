import os
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

import win32file, win32con

pat="C:\\Users\\marco\\Desktop\\imm"
mylist = os.listdir(pat)

a=len(mylist)-2
arr=[None]*a

ai=0
for i in mylist:
    try:
        image=Image.open(i)
        print(i)
        h=i



        if not h[0:4].isdigit():
            if h[0:8]=="Snapchat":
                h=h.replace("Snapchat-","")
            elif h[0:10]=="Screenshot":
                h=h.replace("Screenshot_","")
                h=h[0:15]
                if not h[8]=="_":
                    h=h.replace(i[8],"_")
            elif h[0:3]=="IMG":
                if h[13:15]=="WA":
                    h=h.replace("IMG-","")
                    h=h[0:8]+"_000000"#gestire minuti
                else:
                    h=h.replace("IMG_","")
                    h=h[0:15]
            elif h[0:6]=="FB_IMG":
                h=h.replace("FB_IMG_","")
            elif h[0:5]=="story":
                h=h.replace("story_","")

        if image._getexif():

            r=0
            va=""
            g=0
            done=False

            for tag, value in image._getexif().items():
                v=str(value)[0:4]
                if v.isdigit():
                    v=int(v)
                    if v==2015 or v==2016 or v==2017 or v==2018 or v==2019 or v==2020 or v==2021 or v==2022:
                       done=True
                       arr[ai]=value;
                       valu=arr[ai][0:16].replace(':','_')
                       image.close()
                       try:
                           os.rename(pat+'\\'+i, pat+'\\'+valu+ '.jpg')
                       except FileExistsError:
                           os.rename(pat+'\\'+i, pat+'\\'+valu+'('+str(r)+')'+ '.jpg')
                           r=r+1
                       ai=ai+1
                       break
                else:
                    if i[0:8].isdigit():
                        va=int(i[0:4])

                        if va==2015 or va==2016 or va==2017 or va==2018 or va==2019 or va==2020 or va==2021 or va==2022:

                            g=i[0:15].replace('_',' ')
                            g=g[0:4]+"_"+g[4:6]+"_"+g[6:8]+" "+g[9:11]+"_"+g[11:13]+"_"+g[13:15]
                            image.close()
                            try:
                                os.rename(pat+'\\'+i, pat+'\\'+g+ '.jpg')
                            except FileExistsError:
                                os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(r)+')'+ '.jpg')
                                r=r+1
                            ai=ai+1
                            done=True
                            break;
                        else:
                            done=True
                            image.close()
                            shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')
                            break;

            if not done:
                for tag, value in image._getexif().items():
                    g+=1
                if g<3:
                    if i[0:8].isdigit():
                        va=int(i[0:4])

                        if va==2015 or va==2016 or va==2017 or va==2018 or va==2019 or va==2020 or va==2021 or va==2022:

                            g=i[0:15].replace('_',' ')
                            g=g[0:4]+"_"+g[4:6]+"_"+g[6:8]+" "+g[9:11]+"_"+g[11:13]+"_"+g[13:15]
                            image.close()
                            try:
                                os.rename(pat+'\\'+i, pat+'\\'+g+ '.jpg')
                            except FileExistsError:
                                os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(r)+')'+ '.jpg')
                                r=r+1
                            ai=ai+1
                            done=True
                        else:
                            image.close()                   #fai lista casuale in boh
                            shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')
                    else:
                        image.close()
                        shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')
                else:
                    image.close()
                    shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')
        else:
            print(h[0:8])
            if h[0:8].isdigit():
                va=int(h[0:4])

                if va==2015 or va==2016 or va==2017 or va==2018 or va==2019 or va==2020 or va==2021 or va==2022:

                    g=h[0:15].replace('_',' ')
                    g=g[0:4]+"_"+g[4:6]+"_"+g[6:8]+" "+g[9:11]+"_"+g[11:13]+"_"+g[13:15]
                    image.close()
                    try:
                        os.rename(pat+'\\'+i, pat+'\\'+g+ '.jpg')
                    except FileExistsError:
                        os.rename(pat+'\\'+i, pat+'\\'+g+'('+str(r)+')'+ '.jpg')
                        r=r+1
                    ai=ai+1
                else:
                    image.close()
                    shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')
            else:
                image.close()
                shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\sbagliate')


    except IOError:
        if i !="test.py" and i !="sbagliate" and i!="boh" and i!="video" and i!="change.py" and i!="change":
            if i[len(i)-4:len(i)]==".mp4":
                image.close()
                shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\video')
                print(i+" is a video")
            else:
                image.close()
                shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\boh')
        else:
            print(i+ " is not an image")

    except PIL.UnidentifiedImageError:
            print(i +" i don't know u")
            image.close()
            shutil.move(pat+'\\'+i,'C:\\Users\\marco\\Desktop\\imm\\boh')
