
import tkinter as tk
from tkinter import ttk
from TCalendar import TreeCalendar

def retrieve_date_via_button():
    """
    Single click desired date and hit button

    """
    k = a.send_selected()
    print(k)

def event_driven_date(event):
    """
    Retrieves date on double click by user

    """
    try:
        g = a.send_selected()
        print(g)
        print(g.year)
        print(g.month)
        print(g.day)
    except AttributeError:
        pass

root = tk.Tk()

a = TreeCalendar(root, background='red', foreground='blue', activebackground='yellow', fieldbackground='black',
                 fontsize='15', calendarcolumnwidth='50', calendarheight='5', arrowsize=50)
root.bind('<Double-Button-1>', event_driven_date)
a.pack()

b = ttk.Button(root, text='Get Date', command=retrieve_date_via_button)

b.pack()

root.mainloop()
"""
Default configuration for TreeCalendar

'background': 'white',
'foreground': 'green',
'activebackground': 'white',
'fieldbackground': 'white',
'font': 'Helvetica',
'fontsize': 12,
'calendarcolumnwidth': 45,
'calendarheight': 6,
'arrowsize': 30



"""

