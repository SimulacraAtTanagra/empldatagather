# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:16:58 2020

@author: sayers
"""

import pyautogui as pig
from time import sleep
import os
from admin import newest


#TODO clean this up using newest
def doit(paths,emplid):
    for file in os.listdir(paths): 
        if file.startswith('ps'): 
            filepath = os.path.join(paths,file)
            newpath= os.path.join(paths,f'{emplid}history.xls')
            os.rename(filepath,newpath) 

#TODO replace this with something respectable from selenium
def pig_nav(emplid):
    sleep(5)
    pig.click(enteremplid)  #this has to be defined
    pig.typewrite(i)
    sleep(1)
    pig.click(search)   #this has to be defined
    sleep(15)
    pig.click(download) #this has to be defined
    sleep(5)

#TODO better error handling for this part please
def main(employees,path):
    for i in employees:
        pig_nav(i)
        try:
            doit(path,i)
        except:
            pass