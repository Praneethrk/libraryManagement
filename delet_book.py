from tkinter import *
import os

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


def login_success_book(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('book Home | Library System')
    login_success_screen.geometry('512x512')
    Label(login_success_screen,text="LIBRRY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(login_success_screen, text='Book Deleted successfully:',font='verdana').pack()
    Label(text='').pack()
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

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global book_ssn
    global bname_book_entry
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

    main_screen.mainloop()


main_page()