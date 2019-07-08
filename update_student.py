from tkinter import *
import os

def stud_verify():
    user = name_stud.get()
    usn = pas
    branch = branch_stud.get()
    dob = dob_stud.get()
    ph = ph_stud.get()

    name_stud_entry.delete(0, END)
    branch_stud_entry.delete(0, END)
    dob_stud_entry.delete(0, END)
    ph_stud_entry.delete(0, END)

    for line in open("student.txt.txt", "r").readlines():
        login_info = line.split()
        if usn == login_info:
            stud_exist()
            return TRUE
    insert_stud(user,usn,branch,dob,ph)

def insert_stud(userr,usnn,branchh,dobb,phh):
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',
          width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Student updated Succesfully!', font='verdana', fg='blue').pack()
    file=open('student.txt.txt','a')
    file.write(usnn)
    file.write(" ")
    file.write(userr)
    file.write(" ")
    file.write(branchh)
    file.write(" ")
    file.write(dobb)
    file.write(" ")
    file.write(phh)
    file.write(" ")
    file.write("\n")

def stud_exist():
    global stud_exist_screen
    password_not_recog_screen = Toplevel(login_success_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='ID Alerady Exist!', font='arial',fg='red').pack()
    Label(text='').pack()
    Button(password_not_recog_screen, text='Try Again',fg='white',bg='blue',font='verdana', command=main_page).pack()

def delete_existing(pas):
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
    Label(password_not_recog_screen,text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Invalid Credentials!',font='verdana').pack()
    Button(password_not_recog_screen, text='Try Again', command=main_page).pack()


def login_success_stud(upas):
    global login_success_screen
    global name_emp_entry
    global name_stud_entry
    global usn_stud
    global usn_stud_entry
    global branch_stud
    global branch_stud_entry
    global dob_stud
    global dob_stud_entry
    global ph_stud
    global ph_stud_entry
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('student Home | Library System')
    login_success_screen.geometry('512x512')
    Label(login_success_screen,text="LIBRRY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(login_success_screen, text='Update:',font='verdana').pack()
    Label(text='').pack()
    for line in open("student.txt.txt", "r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(login_success_screen, text='Name:',font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            name_stud_entry = Entry(login_success_screen,textvariable=name_stud)
            name_stud_entry.pack()
            Label(login_success_screen, text='USN:', font='verdana', fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text=login_info[0], font='verdana').pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Branch:', font='verdana', fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            branch_stud_entry = Entry(login_success_screen, textvariable=branch_stud)
            branch_stud_entry.pack()
            Label(login_success_screen, text='DOB:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            dob_stud_entry = Entry(login_success_screen,textvariable=dob_stud)
            dob_stud_entry.pack()
            Label(login_success_screen, text='Phone No:', font='verdana',fg='blue').pack()
            Label(text='').pack()
            Label(text='').pack()
            ph_stud_entry = Entry(login_success_screen,textvariable=ph_stud)
            ph_stud_entry.pack()
        else:
            continue

    Button(login_success_screen, text='Update Student!', font='verdana', fg='white', bg='blue',command=stud_verify).pack()

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global stud_ssn
    global name_emp_entry
    global name_stud
    global name_stud_entry
    global usn_stud
    global usn_stud_entry
    global branch_stud
    global branch_stud_entry
    global dob_stud
    global dob_stud_entry
    global ph_stud
    global ph_stud_entry
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
    name_stud = StringVar()
    usn_stud = StringVar()
    branch_stud = StringVar()
    dob_stud = StringVar()
    ph_stud = StringVar()

    main_screen.mainloop()


main_page()