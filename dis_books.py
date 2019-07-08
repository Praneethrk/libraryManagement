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
    Label(login_success_screen, text='Book Details Are:',font='verdana').pack()
    Label(text='').pack()
    for line in open("books.txt.txt","r").readlines():
        login_info = line.split()
        if pas == login_info[0]:
            Label(login_success_screen, text='Book Name:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[1],font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Book ID:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[0],font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Author:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[2], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Edition:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[3], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()

        else:
            continue


    Button(login_success_screen, text='OK', command=delete_login_success).pack()

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