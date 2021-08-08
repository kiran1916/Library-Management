# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:30:59 2021

@author: saiki
"""

def listSplit():
    global bookname
    global authorname
    global quantity
    global pages
    global year
    global ISBN
    global id
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    pages =[]
    year =[]
    id =[]
    cost =[]
    with open("stock.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    pages.append(a)
                elif(ind==4):
                    year.append(a)
                elif(ind==5):
                    id.append(a)
                elif(ind==6):
                    cost.append(a)
                ind+=1
