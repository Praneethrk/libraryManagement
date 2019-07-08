from tkinter import *
import os

def stud_verify():
    user = name_stud.get()
    usn = usn_stud.get()
    branch = branch_stud.get()
    dob = dob_stud.get()
    ph = ph_stud.get()

    name_stud_entry.delete(0, END)
    usn_stud_entry.delete(0, END)
    branch_stud_entry.delete(0, END)
    dob_stud_entry.delete(0, END)
    ph_stud_entry.delete(0, END)

    for line in open("student.txt.txt", "r").readlines():
        login_info = line.split()
        if usn == login_info:
            stud_exist()
            return TRUE
    insert_stud(user,usn,branch,dob,ph)


def stud_exist():
    global stud_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='ID Alerady Exist!', font='arial',fg='red').pack()
    Label(text='').pack()
    Button(password_not_recog_screen, text='Try Again',fg='white',bg='blue',font='verdana', command=main_page).pack()

def insert_stud(userr,usnn,branchh,dobb,phh):
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('ADMIN Signup | library System')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana',
          width="512", height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Student Added Succesfully!', font='verdana',fg='blue').pack()
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



def main_page():
    global main_screen
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
    main_screen.title('Add Student | Library System')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='blue', fg='white', font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Label(main_screen,text="Enter Details:",font='verdana',fg='blue').pack()
    Label(text='').pack()
    name_stud = StringVar()
    usn_stud = StringVar()
    branch_stud = StringVar()
    dob_stud = StringVar()
    ph_stud = StringVar()

    Label(main_screen, text='Name:', font='verdana', fg='blue').pack()
    name_stud_entry = Entry(main_screen, textvariable=name_stud)
    name_stud_entry.pack()

    Label(main_screen, text='Student ID:', font='verdana', fg='blue').pack()
    usn_stud_entry = Entry(main_screen, textvariable=usn_stud)
    usn_stud_entry.pack()

    Label(main_screen, text='Branch:', font='verdana', fg='blue').pack()
    branch_stud_entry = Entry(main_screen, textvariable=branch_stud)
    branch_stud_entry.pack()

    Label(main_screen, text='DOB:', font='verdana', fg='blue').pack()
    dob_stud_entry = Entry(main_screen, textvariable=dob_stud)
    dob_stud_entry.pack()

    Label(main_screen, text='Phone No:', font='verdana', fg='blue').pack()
    ph_stud_entry = Entry(main_screen, textvariable=ph_stud)
    ph_stud_entry.pack()
    Label(text='').pack()

    Button(main_screen, text='Add Student!', width=20, height=2, font='verdana', fg='white', bg='blue',command=stud_verify).pack()

    main_screen.mainloop()

main_page()