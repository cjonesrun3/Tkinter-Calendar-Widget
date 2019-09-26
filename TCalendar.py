# !Python3
# 26APR2019
# BY: C.R. JONES
# PYTHON VERSION 3.6.1
"""
This is my attempt to utilize the treeview widget to create a calendar widget.


"""


import calendar
from tkinter import *
from tkinter import ttk



class TreeCalendar(ttk.Frame):
    date = calendar.datetime.date
    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta
    strptime = calendar.datetime.datetime.strptime


    def __init__(self, master=None, **kw):
        """
        Actual Widget

        """
        ttk.Frame.__init__(self, master)

        tree_frame = ttk.Frame(self)

        style = ttk.Style()

        style.configure('Treeview', background='white', foreground='green', activebackground='grey')
        style.configure('Treeview.Heading', foreground='green', background='grey')

        self.tree_headers = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
        # DIR_TREE_CONFIG
        self.tree = ttk.Treeview(tree_frame, columns=self.tree_headers)

        self.tree['show'] = 'headings'

        self.tree.configure(height=50)

        self.tree.heading('Mon', text='Mon', anchor=W)
        self.tree.heading('Tue', text='Tue', anchor=W)
        self.tree.heading('Wed', text='Wed', anchor=W)
        self.tree.heading('Thur', text='Thur', anchor=W)
        self.tree.heading('Fri', text='Fri', anchor=W)

        self.tree.pack()