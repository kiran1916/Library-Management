# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:31:40 2021

@author: saiki
"""

def getDate():
    import datetime
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
