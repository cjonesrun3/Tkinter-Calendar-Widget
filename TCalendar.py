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
                        self.year_frame
                        self.month_frame
                        self.tree_frame


        """

        ttk.Frame.__init__(self, master)  # Base frame
        style = ttk.Style()
        passed_kws = list(kw.keys())  # Properties passed by user

        print(passed_kws)
        # *************************************************************************************************************
        # Takes in properties
        # *************************************************************************************************************
        options = [
            'background',
            'foreground',
            'activebackground',

        ]
        for passed in passed_kws:  # Clears bad arguments kws
            if passed not in options:
                del(kw[passed])

        self._selected_options = {
            'background': 'white',
            'foreground': 'green',
            'activebackground': 'grey'
        }
        self._selected_options.update(kw)  # Updates defaults with user kws
        # *************************************************************************************************************
        # self.year_frame
        # *************************************************************************************************************
        self.year_frame = ttk.Frame(self)
        self.year = str(self.datetime.year)
        self.year_label = ttk.Label(self.year_frame, text=self.year)
        self.year_forward_button = ttk.Button()

        self.year_label.pack()
        # *************************************************************************************************************
        # self.month_frame
        # *************************************************************************************************************
        self.month_frame = ttk.Frame(self)
        self.month = str(self.datetime.month)
        self.month_label = ttk.Label(self.month_frame, text=self.month, background=self._selected_options['background'])

        self.month_label.pack()
        # *************************************************************************************************************
        # self.tree_frame
        # *************************************************************************************************************
        self.tree_frame = ttk.Frame(self)

        style.configure('Treeview', background=self._selected_options['background'],
                        foreground='green', activebackground='grey')
        style.configure('Treeview.Heading', foreground=self._selected_options['foreground'], background='grey')

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
        self.year_frame.grid(column=0, row=0)
        self.month_frame.grid(column=0, row=1)
        self.tree_frame.grid(column=0, row=2)
