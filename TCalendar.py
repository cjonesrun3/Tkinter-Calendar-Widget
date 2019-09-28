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
        self.style = ttk.Style(self)
        self.style.theme_use('clam')  # Ensures treeview initiates with activebackground

        passed_kws = list(kw.keys())  # Properties passed by user
        # *************************************************************************************************************
        # Takes in properties
        # *************************************************************************************************************
        options = [
            'background',
            'foreground',
            'activebackground',
            'fieldbackground',
            'font',
            'fontsize',
            'calendarcolumnwidth',
            'calendarheight',
            'alternatingrowcolor',
            'evenrowcolor',
            'oddrowcolor',
            'arrowsize'

        ]
        for passed in passed_kws:  # Clears bad arguments from kws
            if passed not in options:
                del(kw[passed])

        self._selected_options = {
            'background': 'white',
            'foreground': 'green',
            'activebackground': 'white',
            'fieldbackground': 'white',
            'font': 'Helvetica',
            'fontsize': 12,
            'calendarcolumnwidth': 45,
            'calendarheight': 6,
            'alternatingrowcolor': 'ENABLED',
            'evenrowcolor': 'grey',
            'oddrowcolor': 'white',
            'arrowsize': 30

        }
        self._selected_options.update(kw)  # Updates defaults with user kws
        # *************************************************************************************************************
        # Sets up configurations for style from arguments passed in kws
        # *************************************************************************************************************
        selected_background = self._selected_options.get('background')
        selected_foreground = self._selected_options.get('foreground')
        selected_activebackground = self._selected_options.get('activebackground')
        selected_fieldbackground = self._selected_options.get('fieldbackground')
        selected_font = self._selected_options.get('font')
        selected_fontsize = self._selected_options.get('fontsize')
        selected_arrowsize = self._selected_options.get('arrowsize')

        self.style.layout('L.TButton',
                          [('Button.focus',
                            {'children': [('Button.leftarrow', None)]})])
        self.style.layout('R.TButton',
                          [('Button.focus',
                            {'children': [('Button.rightarrow', None)]})])

        self.style.configure('TFrame', background=selected_background)

        self.style.configure('Treeview', background=selected_background,
                             foreground=selected_foreground, activebackground=selected_activebackground,
                             fieldbackground=selected_fieldbackground)

        self.style.configure('Treeview.Heading', foreground=selected_foreground, background=selected_background,
                             activebackground=selected_activebackground, font=(selected_font, int(selected_fontsize)))

        self.style.configure('TLabel', background=selected_background, font=(selected_font, int(selected_fontsize)))

        self.style.configure('R.TButton', background=selected_background,
                             arrowcolor=selected_foreground, bordercolor=selected_background,
                             relief="flat", lightcolor=selected_background, darkcolor=selected_background,
                             arrowsize=int(selected_arrowsize))

        self.style.configure('L.TButton', background=selected_background, arrowcolor=selected_foreground,
                             bordercolor=selected_background, relief="flat", lightcolor=selected_background,
                             darkcolor=selected_background, arrowsize=int(selected_arrowsize))

        # *************************************************************************************************************
        # self.year_frame
        # *************************************************************************************************************
        self.year_frame = ttk.Frame(self)
        self.year_frame.configure(style='TFrame')
        self.year = str(self.date.today().year)
        self.year_label = ttk.Label(self.year_frame, text=self.year, style='TLabel')
        self.year_forward_button = ttk.Button(self.year_frame, style='R.TButton')
        self.year_back_button = ttk.Button(self.year_frame, style='L.TButton')

        self.year_back_button.grid(column=0, row=0)
        self.year_label.grid(column=1, row=0)
        self.year_forward_button.grid(column=2, row=0)

        # *************************************************************************************************************
        # self.month_frame
        # *************************************************************************************************************
        self.month_frame = ttk.Frame(self)
        self.month_frame.configure(style='TFrame')
        self.month = str(self.date.today().strftime('%B'))
        self.month_label = ttk.Label(self.month_frame, text=self.month, style='TLabel')
        self.month_forward_button = ttk.Button(self.month_frame, style='R.TButton')
        self.month_back_button = ttk.Button(self.month_frame, style='L.TButton')

        self.month_back_button.grid(column=0, row=0)
        self.month_label.grid(column=1, row=0)
        self.month_forward_button.grid(column=2, row=0)
        # *************************************************************************************************************
        # self.tree_frame
        # *************************************************************************************************************
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.configure(style='TFrame')

        self.tree_headers = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

        self.tree = ttk.Treeview(self.tree_frame, columns=self.tree_headers)

        self.tree['show'] = 'headings'
        self.tree.configure(height=int(self._selected_options.get('calendarheight')))
        self.tree.heading('Mon', text='Mon', anchor=N)
        self.tree.heading('Tue', text='Tue', anchor=N)
        self.tree.heading('Wed', text='Wed', anchor=N)
        self.tree.heading('Thr', text='Thr', anchor=N)
        self.tree.heading('Fri', text='Fri', anchor=N)
        self.tree.heading('Sat', text='Sat', anchor=N)
        self.tree.heading('Sun', text='Sun', anchor=N)

        self.set_tree_column_width = int(self._selected_options.get('calendarcolumnwidth'))

        self.tree.column('Mon', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Tue', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Wed', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Thr', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Fri', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Sat', width=self.set_tree_column_width, anchor=N)
        self.tree.column('Sun', width=self.set_tree_column_width, anchor=N)

        self.tree.pack(fill=BOTH, expand=1)
        # *************************************************************************************************************
        # Frame packing
        # *************************************************************************************************************
        self.year_frame.grid(column=0, row=0)
        self.month_frame.grid(column=0, row=1)
        self.tree_frame.grid(column=0, row=2)

        self.tree.bind('<Button-1>', self.selectItem)


        self._update_calendar()

    def _update_calendar(self):
        current_year = self.date.today().year
        current_month = self.date.today().month
        # Below returns the first weekday of the month and number of days in the month
        current_month = calendar.monthcalendar(current_year, current_month)

        for day in current_month:
            print(day)
            self.tree.insert('', 'end', values=(day))  # INSERTS DATA INTO TREEVIEW





    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)

        if col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        elif col == '#4':
            cell_value = curItem['values'][3]
        elif col == '#5':
            cell_value = curItem['values'][4]
        elif col == '#6':
            cell_value = curItem['values'][5]
        elif col == '#7':
            cell_value = curItem['values'][6]

        print('cell_value = ', cell_value)
        print(type(cell_value))




"""
TODO:
1) Possibly use global month number and year variable to ensure smooth transition of months and years
2) Figure out how to pull data


"""


