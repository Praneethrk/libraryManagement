from tkinter import *
import os

def book_verify():
    bname = bname_book.get()
    bid = pas
    author = author_book.get()
    edition = edition_book.get()

    bname_book_entry.delete(0, END)
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
    Label(password_not_recog_screen, text='Book Updated Succesfully!', font='verdana',fg='blue').pack()
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

def delete_existing(pas):
    temp = list()
    fhand = open("books.txt.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("books.txt.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')



def login_verify_book():
    password1 = book_ssn.get()

    for line in open("books.txt.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_book(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Login Error | Library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen,text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Invalid Credentials!',font='verdana').pack()
    Button(password_not_recog_screen, text='Try Again', command=main_page).pack()


def login_success_book(upas):
    global login_success_screen
    global bname_book
    global bname_book_entry
    global bid_book
    global bid_book_entry
    global author_book
    global author_book_entry
    global edition_book
    global edition_book_entry
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('book Home | Library System')
    login_success_screen.geometry('512x512')
    Label(login_success_screen,text="LIBRRY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(login_success_screen, text='Book Details Are:',font='verdana').pack()
    Label(text='').pack()
    for line in open("books.txt.txt","r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(login_success_screen, text='Book Name:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            bname_book_entry = Entry(login_success_screen, textvariable=bname_book)
            bname_book_entry.pack()
            Label(login_success_screen, text='Book ID:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[0],font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Author:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            author_book_entry = Entry(login_success_screen, textvariable=author_book)
            author_book_entry.pack()
            Label(login_success_screen, text='Edition:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            edition_book_entry = Entry(login_success_screen, textvariable=edition_book)
            edition_book_entry.pack()

        else:
            continue

    Button(login_success_screen, text='Add Book!', width=20, height=2, font='verdana', fg='white', bg='blue', command=book_verify).pack()
def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global book_ssn
    global bname_book_entry
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
    main_screen.title('View Book | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(main_screen,text="Enter the book id:",font='verdana',fg='blue').pack()
    Label(text='').pack()
    Label(text='').pack()
    book_ssn=StringVar()
    bname_book_entry= Entry(main_screen, textvariable=book_ssn)
    bname_book_entry.pack()
    Label(text=' ').pack()
    Button(text='Enter', height='2', width='30', font='verdana',fg='white',bg='blue',command=login_verify_book).pack()
    Label(text='').pack()
    bname_book = StringVar()
    bid_book = StringVar()
    author_book = StringVar()
    edition_book = StringVar()
    main_screen.mainloop()


main_page()