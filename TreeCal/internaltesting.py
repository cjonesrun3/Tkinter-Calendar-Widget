from TCalendar import TreeCalendar
import tkinter as tk
from tkinter import ttk
def retrieve_date_via_button():
    """
    Single click desired date and hit button
    """
    k = a.send_selected()  # send_selected() method retrieves datetime object
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

b = TreeCalendar(root)

b.pack()

get_date_of_selected_date_by_button = ttk.Button(root, text='Get Date', command=retrieve_date_via_button)

get_date_of_selected_date_by_button.pack()

root.mainloop()