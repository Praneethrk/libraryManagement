from tkinter import *
import os


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.title('View Book | Library System')
    main_screen.geometry('512x512')
    frame = Frame(main_screen)
    grid=Frame(frame)
    Label(main_screen, text="Books Available",font='verdana',fg='blue').grid(row=0, column=1, columnspan=4)
    Label(main_screen, text='Book ID ',font='verdana',fg='blue').grid(row=1, column=0)
    Label(main_screen, text='       ',font='verdana',fg='blue').grid(row=1, column=1)
    Label(main_screen, text='Book Name ',font='verdana',fg='blue').grid(row=1, column=2)
    Label(main_screen, text='       ',font='verdana',fg='blue').grid(row=1, column=3)
    Label(main_screen, text='Book Author ',font='verdana',fg='blue').grid(row=1, column=4)
    i=2
    for line in open("books.txt.txt","r").readlines():
        book = line.split()
        Label(main_screen, text=book[0],font='verdana').grid(row=i, column=0)
        Label(main_screen, text=book[1],font='verdana').grid(row=i, column=2)
        Label(main_screen, text=book[2],font='verdana').grid(row=i, column=4)
        i = i + 1

    main_screen.mainloop()
    
    
main_page()    