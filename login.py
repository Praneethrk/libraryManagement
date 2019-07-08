from tkinter import *
from tkinter import messagebox
import os


def add_book():
    os.system('python add_books.py')

def add_stud():
    os.system('python add_student.py')

def update_stud():
    os.system('python update_student.py')

def delete_stud():
    os.system('python delete_student.py')

def dis_book():
    os.system('python dis_books.py')

def dis_stud():
    os.system('python dis_student.py')

def update_book():
    os.system('python update_book.py')

def del_book():
    os.system('python delet_book.py')

def book_issue():
    os.system('python book_issue.py')

def book_deposite():
    os.system('python book_deposite.py')

def display_book():
    os.system('python display_book.py')

def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = Toplevel(main_screen)
    login_screen.title('Admin Login | Library System')
    login_screen.geometry('512x512')
    Label(login_screen, text='Please Enter your Credentials below',font='verdana').pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username',font='verdana').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='').pack()
    Label(login_screen, text='Password',font='verdana').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text='').pack()
    Button(login_screen, text='Login', width=10, height=1,font='verdana', command=login_verify).pack()




def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    for line in open("login.txt", "r").readlines():
        login_info = line.split()
        if username1 == login_info[0] and password1 == login_info[1]:
            login_success()
            return TRUE
    password_not_recognised()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Login Success')
    login_success_screen.geometry('312x312')
    Label(login_success_screen, text='Login Success').pack()
    Button(login_success_screen, text='Continue', command=admin_button()).pack()



def admin_button():
    Button(login_success_screen, text='Add new Student!', font='verdana', height=2, width=30, fg='white', bg='blue',command=add_stud).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='View Existing Student!', font='verdana', height=2, width=30, fg='white', bg='blue',command=dis_stud).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Update Existing Student!', font='verdana', height=2, width=30, fg='white', bg='blue',command=update_stud).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Remove Existing Student!', font='verdana', height=2, width=30, fg='white', bg='blue',command=delete_stud).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Add new Book!', font='verdana', height=2, width=30, fg='white', bg='blue',command=add_book).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='View Existing Book!', font='verdana', height=2, width=30, fg='white', bg='blue',command=dis_book).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Update Existing Book!', font='verdana', height=2, width=30, fg='white', bg='blue',command=update_book).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Remove Existing Book!', font='verdana', height=2, width=30, fg='white',bg='blue',command=del_book).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Book issue', font='verdana', height=2, width=30, fg='white',bg='blue', command = book_issue).pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(login_success_screen, text='Book deposite', font='verdana', height=2, width=30, fg='white',bg='blue', command = book_deposite).pack()
    Label(text='').pack()
    Label(text='').pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title('Invalid Password')
    password_not_recog_screen.geometry('312x312')
    Label(password_not_recog_screen, text='Invalid Password').pack()
    Button(password_not_recog_screen, text='OK', command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('User not found')
    user_not_found_screen.geometry('212x212')
    Label(user_not_found_screen, text='User not found').pack()
    Button(user_not_found_screen, text='OK', command=delete_user_not_found).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found():
    user_not_found_screen.destroy()




def student():
    global student_display
    student_display = Toplevel(main_screen)
    student_display.title('Student | Library System')
    student_display.geometry('512x512')
    Button(student_display, text='Display Books!', font='verdana', height='2', width='30', fg='white', bg='blue',command=display_book).pack()
    Label(text='').pack()
    Label(text='').pack()
    

def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("512x512")
    main_screen.title('Welcome|Library Management')
    Label(text="LIBRARY MANAGEMENT SYSTEM", bg='grey',fg='white',font='verdana', width="512", height="2").pack()
    Label(text='').pack()
    Button(text='ADMIN', height='2', width='30',font='verdana', command=login).pack()
    Label(text=' ').pack()
    Button(text='STUDENT', height='2', width='30',font='verdana', command=student).pack()
    Label(text=' ').pack()
    

    main_screen.mainloop()


main_page()

