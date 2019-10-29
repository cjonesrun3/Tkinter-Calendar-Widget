# Tkinter Calendar Widget
 A simple calendar widget that uses the ttk treeview as a base. 
 
 **INSTALL**
 
 Just drop the TreeCalendar directory into your sitepackages and see the code below as an example of configuration options and use. 

![alt text](https://github.com/cjonesrun3/Tkinter-Calendar-Widget/blob/master/TreeCalImg.PNG)

**EXAMPLE OF USE**

```python
import tkinter as tk
from tkinter import ttk
from TreeCal import TreeCalendar

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

get_date_of_selected_date_by_button = ttk.Button(root, text='Get Date', command=retrieve_date_via_button)

get_date_of_selected_date_by_button.pack()

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
```
