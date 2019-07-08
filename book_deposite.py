from tkinter import *
from datetime import datetime
import datetime
import os

def login_verify_stud():
    password1 = stud_ssn.get()
    password2 = book_ssn.get()
    global str
    str = 'Please enter the valid id'
    for line in open("book_issued.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            if password2 == login_info[1]:
                deposite_book()
                return TRUE
    password_not_recognised(str)


def password_not_recognised(str):
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Login Error | Library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen,text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text=str,font='verdana').pack()
    Button(password_not_recog_screen, text='Try Again', command=main_page).pack()

def deposite_book():
    global issue_book_screen
    global d
    bssn = book_ssn.get()
    sssn = stud_ssn.get()
    issue_book_screen = Toplevel(main_screen)
    issue_book_screen.title('book deposite | Library System')
    issue_book_screen.geometry('512x512')
    Label(issue_book_screen, text="LIBRRY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(issue_book_screen, text='Book deposited Successfully', font='verdana').pack()
    Label(text='').pack()
    d = datetime.date.today()

    temp1 = list()
    fhand = open("book_issued.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        login_info = record.split()
        if record.startswith(sssn):
            if bssn == login_info[1]:
                s = record
                file = open("issued_history.txt", "a")
                file.write(record)
                file.write(" ")
                file.write(d.strftime('%d/%m/%Y'))
                file.write(" ")
                file.write('\n')
                file.close()
            else:
                temp1.append(record)
        else:
            temp1.append(record)
    del temp1[-1]

    fhand = open("book_issued.txt", "r")
    data = fhand.readlines()
    f = open("book_issued.txt", 'w')
    for line in data:
        if line.strip("\n") != s:
            f.write(line)



def main_page():
    global main_screen
    global book_ssn
    global stud_ssn
    global bname_book_entry
    global sname_student_entry
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Book issue | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(main_screen,text="Enter the book id:",font='verdana',fg='blue').pack()
    Label(text='').pack()
    Label(text='').pack()
    book_ssn = StringVar()
    bname_book_entry= Entry(main_screen, textvariable=book_ssn)
    bname_book_entry.pack()
    Label(text=' ').pack()
    Label(main_screen, text="Enter the student id:", font='verdana', fg='blue').pack()
    Label(text='').pack()
    Label(text='').pack()
    stud_ssn = StringVar()
    sname_student_entry = Entry(main_screen, textvariable=stud_ssn)
    sname_student_entry.pack()
    Label(text=' ').pack()
    Button(text='Enter', height='2', width='30', font='verdana',fg='white',bg='blue', command=login_verify_stud).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()