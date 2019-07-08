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
    global deleted_success
    deleted_success = Toplevel(main_screen)
    deleted_success.title('Login Error | Library System')
    deleted_success.geometry('312x312')
    Label(deleted_success,text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(deleted_success, text='Invalid Credentials!',font='verdana').pack()
    Button(deleted_success, text='Try Again', command=main_page).pack()


def login_success_stud(pas):
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',
          width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Student deleted Succesfully!', font='verdana', fg='blue').pack()
    temp = list()
    fhand = open("student.txt.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("student.txt.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')




def main_page():
    global main_screen
    global stud_ssn
    global name_emp_entry
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('View Student | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
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
    Button(text='Enter', height='2', width='30', font='verdana',fg='white',bg='blue',command=login_verify_stud).pack()
    Label(text='').pack()

    main_screen.mainloop()


main_page()