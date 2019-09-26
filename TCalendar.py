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

        ________________________________________________


        """

        ttk.Frame.__init__(self, master)  # Base frame
        # *************************************************************************************************************
        # Month - Year frame
        # *************************************************************************************************************
        self.month_year_frame = ttk.Frame(self)
        self.month_year = str(self.datetime.month)
        self.month_year_label = ttk.Label(self.month_year_frame, text=self.month_year)

        self.month_year_label.pack()
        # *************************************************************************************************************
        # self.tree_frame
        # *************************************************************************************************************
        self.tree_frame = ttk.Frame(self)

        style = ttk.Style()

        style.configure('Treeview', background='white', foreground='green', activebackground='grey')
        style.configure('Treeview.Heading', foreground='green', background='grey')

        self.tree_headers = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

        self.tree = ttk.Treeview(self.tree_frame, columns=self.tree_headers)

        self.tree['show'] = 'headings'

        self.tree.configure(height=10)
        self.tree.heading('Sun', text='Sun', anchor=W)
        self.tree.heading('Mon', text='Mon', anchor=W)
        self.tree.heading('Tue', text='Tue', anchor=W)
        self.tree.heading('Wed', text='Wed', anchor=W)
        self.tree.heading('Thur', text='Thur', anchor=W)
        self.tree.heading('Fri', text='Fri', anchor=W)
        self.tree.heading('Sat', text='Sat', anchor=W)

        self.set_tree_column_width = 40
        self.tree.column('Sun', width=self.set_tree_column_width)
        self.tree.column('Mon', width=self.set_tree_column_width)
        self.tree.column('Tue', width=self.set_tree_column_width)
        self.tree.column('Wed', width=self.set_tree_column_width)
        self.tree.column('Thur', width=self.set_tree_column_width)
        self.tree.column('Fri', width=self.set_tree_column_width)
        self.tree.column('Sat', width=self.set_tree_column_width)


        self.tree.pack()
        # *************************************************************************************************************
        # Frame packing
        # *************************************************************************************************************
        self.month_year_frame.grid(column=0, row=0)
        self.tree_frame.grid(column=0, row=1)
