# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 00:13:43 2021

@author: saiki
"""

def add_book(file="stock.txt"):
    bookname = input('bookname: ')
    authorname = input('authorname: ')
    quantity = input('quantity: ')
    pages = input('pages: ')
    year = input('year: ')
    ISBN = input('ISBN: ')
    id = input('id: ')
    cost = input('cost: ')
    

    with open(file, 'a') as myFile:
        myFile.write((bookname) + ',' + (authorname) + ',' + (quantity) + ',' + (pages) + ',' + (year) + ',' + (ISBN) + ',' + (id) + ','+ (cost) +  '\n')


def delete_book(file="stock.txt"):
    bookname = input('bookname: ')
    authorname = input('authorname: ')
    quantity = input('quantity: ')
    pages = input('pages: ')
    year = input('year: ')
    ISBN = input('ISBN: ')
    id = input('id: ')
    cost = input('cost: ')
    

    with open(file, 'r') as myFile:
        text = myFile.read()

    text = text.replace((bookname) + ',' + (authorname) + ',' + (quantity) + ',' + (pages) + ',' + (year) + ',' + (ISBN) + ',' + (id) + ','+ (cost) +  '\n')

    with open(file, 'w') as myFile:
        myFile.write(text)
