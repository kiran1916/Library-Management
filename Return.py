# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:34:32 2021

@author: saiki
"""
import dt
import ListSplit

def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b= "Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tcost\n")


    total=0.0
    for i in range(3):
         if ListSplit.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.cost[i]+"\n")
                ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            
            
    print("\t\t\t\t\t\t\t"+"R"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=100*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: R"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "R"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: R"+ str(total))
    
        
    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+ListSplit.pages[i]+","+ListSplit.year[i]+","+ListSplit.id[i]+","+ListSplit.cost[i]+"\n")