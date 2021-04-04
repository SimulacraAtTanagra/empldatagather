# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:16:58 2020

@author: sayers
"""

import pandas as pd
import pyautogui as pig
from time import sleep
from datetime import datetime
import os
from os import path
import re
import numpy as np
import win32com.client as win32

def doit(emplid):
    paths = 'S:\\downloads\\'
    for root, dirs, files in os.walk(paths): 
        for file in files:  
      
            # change the extension from '.mp3' to  
            # the one of your choice. 
            if file.startswith('ps'): 
                filepath = str(paths+file)
                os.rename(f'{emplid}history.xls') 
"""
sleep(5)
enteremplid = (171,307)

search = (39, 427)

download  = (628, 223)

returntostart= (593, 119)
"""
for i in employees:
    emplid = i
    sleep(5)
    pig.click(enteremplid)
    pig.typewrite(i)
    sleep(1)
    pig.click(search)
    sleep(15)
    pig.click(download)
    sleep(5)
    try:
        doit(i)
    except:
        pass