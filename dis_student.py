from tkinter import *
import os

def login_verify_stud():
    password1 = stud_ssn.get()


    for line in open("student.txt.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_stud(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Login Error | Library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen,text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='yellow', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Invalid Credentials!',font='verdana').pack()
    Button(password_not_recog_screen, text='Try Again', command=main_page).pack()


def login_success_stud(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('student Home | Library System')
    login_success_screen.geometry('512x512')
    Label(login_success_screen,text="LIBRRY MANAGEMENT SYSTEM", bg='blue', fg='yellow', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(login_success_screen, text='Your Details Are:',font='verdana').pack()
    Label(text='').pack()
    for line in open("student.txt.txt", "r").readlines():
        login_info = line.split()
        if pas == login_info[0]:
            Label(login_success_screen, text='Name:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[1],font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='USN:', font='verdana', fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[0], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Branch:', font='verdana', fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[2], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='DOB:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[3], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Phone No:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[4], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
        else:
            continue


    Button(login_success_screen, text='OK', command=delete_login_success).pack()

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global stud_ssn
    global name_emp_entry
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('View Student | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='yellow', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(text='').pack()
    Label(main_screen,text="Enter the usn of student:",font='verdana',fg='blue').pack()
    Label(text='').pack()
    Label(text='').pack()
    stud_ssn=StringVar()
    name_stud_entry = Entry(main_screen, textvariable=stud_ssn)
    name_stud_entry.pack()
    Label(text=' ').pack()
    Button(text='Enter', height='2', width='30', font='verdana',fg='yellow',bg='blue',command=login_verify_stud).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()
