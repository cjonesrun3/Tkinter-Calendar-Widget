
import tkinter as tk
from tkinter import ttk
from TCalendar import TreeCalendar

def alternate():
    k = a.send_selected()
    print(k)

def open_it(event):
    """
    Use send_selected() method to get return datetime

    """
    g = a.send_selected()
    print(g)
    print(g.year)
    print(g.month)
    print(g.day)

root = tk.Tk()
root.configure()
a = TreeCalendar(root)
root.bind('<Double-Button-1>', open_it)
a.pack()
b = ttk.Button(root, text='BUUTAN', command=alternate)


b.pack()
root.mainloop()
"""
background='red', foreground='blue', activebackground='yellow', fieldbackground='black',
                 fontsize='20', calendarcolumnwidth='100', calendarheight='20', arrowsize=30






"""
