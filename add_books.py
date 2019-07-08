from tkinter import *
import os

def book_verify():
    bname = bname_book.get()
    bid = bid_book.get()
    author = author_book.get()
    edition = edition_book.get()

    bname_book_entry.delete(0, END)
    bid_book_entry.delete(0, END)
    author_book_entry.delete(0, END)
    edition_book_entry.delete(0, END)

    for line in open("books.txt.txt", "r").readlines():
        login_info = line.split()
        if bid == login_info:
            book_exist()
            return TRUE
    insert_book(bname,bid,author,edition)

def book_exist():
    global book_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='ID Alerady Exist!', font='arial',fg='red').pack()
    Label(text='').pack()
    Button(password_not_recog_screen, text='Try Again',fg='white',bg='blue',font='verdana', command=main_page).pack()

def insert_book(bnamee,bidd,authorr,editionn):
    global book_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Book Added Succesfully!', font='verdana',fg='blue').pack()
    file=open('books.txt.txt','a')
    file.write(bidd)
    file.write(" ")
    file.write(bnamee)
    file.write(" ")
    file.write(authorr)
    file.write(" ")
    file.write(editionn)
    file.write(" ")
    file.write("\n")



def main_page():
    global main_screen
    global bname_book
    global bname_book_entry
    global bid_book
    global bid_book_entry
    global author_book
    global author_book_entry
    global edition_book
    global edition_book_entry
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Add Student | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(main_screen,text="Enter Details:",font='verdana',fg='blue').pack()
    Label(text='').pack()
    bname_book = StringVar()
    bid_book = StringVar()
    author_book = StringVar()
    edition_book = StringVar()

    Label(main_screen, text='Name:', font='verdana', fg='blue').pack()
    bname_book_entry = Entry(main_screen, textvariable=bname_book)
    bname_book_entry.pack()
    Label(main_screen, text='Book ID:', font='verdana', fg='blue').pack()
    bid_book_entry = Entry(main_screen, textvariable=bid_book)
    bid_book_entry.pack()
    Label(main_screen, text='Author', font='verdana', fg='blue').pack()
    author_book_entry = Entry(main_screen, textvariable=author_book)
    author_book_entry.pack()
    Label(main_screen, text='Edition', font='verdana', fg='blue').pack()
    edition_book_entry = Entry(main_screen, textvariable=edition_book)
    edition_book_entry.pack()
    Label(text='').pack()

    Button(main_screen, text='Add Book!', width=20, height=2, font='verdana', fg='white', bg='blue', command=book_verify).pack()

    main_screen.mainloop()

main_page()