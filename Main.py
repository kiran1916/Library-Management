# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:55:39 2021

@author: saiki
"""

import ListSplit
import Borrow
import Return
import addremove

def create_account(file="user.txt"):
    username = input('username: ')
    password = input('password: ')
    name = input('name: ')
    location = input('location: ')
    age = input('age: ')
    contact = input('contact: ')

    with open(file, 'a') as myFile:
        myFile.write((username) + ',' + (password) + ',' + (name) + ',' + (location) + ',' + (age) + ',' + (contact) + '\n')


def delete_account(file="user.txt"):
    account = input('which account would you like to delete? ')
    password = input("please verify your account's password: ")
    name = input('name: ')
    location = input('location: ')
    age = input('age: ')
    contact = input('contact: ')

    with open(file, 'r') as myFile:
        text = myFile.read()

    text = text.replace((account) + ',' + (password) + ',' + (name) + ',' + (location) + ',' + (age) + ',' + (contact) + '\n')

    with open(file, 'w') as myFile:
        myFile.write(text)


def login(file='user.txt'):
    account = input('username: ')
    password = input("password: ")

    with open(file, 'r') as myFile:
        text = myFile.read()

    find_account = text.find((account) + ',' + (password) + '\n')

    if find_account != -1:
        print('welcome, ' + account)
    else:
        print('no such user or incorrect password')



def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. for Admin")
        print("Enter 2. for borrower")
        try:
            a=int(input("Select a choice from 1-2: "))
            print()
            if(a==1):
               # print("hello Admin! how are you today?")
               login() 
               while(True):
                   # print("hello Admin! Please select a choice below: ")
                    print('\n' *5)
                    print("Enter 1 to Display all books")
                    print("Enter 2 to Add a book")
                    print("Enter 3 to return a book")
                    print("Enter 4 to borrow a book")
                    print("Enter 5 to add more members")
                    print("Enter 6 to Exit")
                    b=int(input("Select choice from 1-6: "))
                    print()
                    if b == 1:
                        with open("stock.txt","r") as f:
                                 lines=f.read()
                                 print(lines)
                                 print ()
                    elif b == 2:
                        addremove.add_book()
                    
                    elif b == 3:
                         ListSplit.listSplit()
                         Return.returnBook()
                    elif b == 4:
                         ListSplit.listSplit()
                         Borrow.borrowBook()
                    elif b == 5:
                        create_account()
                          
                    else:
                        print("Thanks for visiting! See you soon!")
                        break     
                            
            elif(a==2):
               # print("Hello User! How are you today?")
                 login()
                 while(True):
                    print('\n' *5)
                   # print("hello user! Please select a choice below: ")
                    print("Enter 1. To Display")
                    print("Enter 2. To Borrow a book")
                    print("Enter 3. To return a book")
                    print("Enter 4. To exit")
                    c=int(input("Select choice from 1-4: "))
                    print()
                    if c == 1:
                        with open("stock.txt","r") as f:
                                 lines=f.read()
                                 print(lines)
                                 print ()
                    elif c == 2:
                        ListSplit.listSplit()
                        Borrow.borrowBook()
                    elif c == 3:
                        ListSplit.listSplit()
                        Return.returnBook()
                    else:
                         print("Thanks for visiting! See you soon!")
                    break
                            
            
            else:
                print("Please enter a valid choice from 1-2")
        
              
        except ValueError:
            print("Please input as suggested.")
start()
