# !Python3
# 29SEP2019
# BY: C.R. JONES
# PYTHON VERSION 3.6.1
"""
This is a simple calendar widget using the treeview widget as the calendar. It returns a datetime object when a user
clicks on a date.


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
        self.currently_displayed_year = StringVar()  # Keeps track of currently displayed year
        self.currently_displayed_month = StringVar()  # Keeps track of currently displayed month

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

        self.style.configure('R.TButton', background=selected_background,
                             arrowcolor=selected_foreground, bordercolor=selected_background,
                             relief="flat", lightcolor=selected_background, darkcolor=selected_background,
                             arrowsize=int(selected_arrowsize))

        self.style.configure('L.TButton', background=selected_background, arrowcolor=selected_foreground,
                             bordercolor=selected_background, relief="flat", lightcolor=selected_background,
                             darkcolor=selected_background, arrowsize=int(selected_arrowsize))

        self.style.configure('TFrame', background=selected_background)

        self.style.configure('Treeview', background=selected_background,
                             foreground=selected_foreground, activebackground=selected_activebackground,
                             fieldbackground=selected_fieldbackground)

        self.style.configure('Treeview.Heading', foreground=selected_foreground, background=selected_background,
                             activebackground=selected_activebackground, font=(selected_font, int(selected_fontsize)))

        self.style.configure('TLabel', background=selected_background, font=(selected_font, int(selected_fontsize)))

        # *************************************************************************************************************
        # self.year_frame
        # *************************************************************************************************************
        self.year_frame = ttk.Frame(self)
        self.year_frame.configure(style='TFrame')
        self.year_label = ttk.Label(self.year_frame, textvariable=self.currently_displayed_year, style='TLabel')
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
        self.month_label = ttk.Label(self.month_frame, textvariable=self.currently_displayed_month, style='TLabel')
        self.month_forward_button = ttk.Button(self.month_frame, style='R.TButton',
                                               command=self._refresh_calendar_month_forward)
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
        # *************************************************************************************************************
        # Bindings
        # *************************************************************************************************************
        # Using single click as a binding generally raises index errors and results in the current selectection being
        # In the same column, but often the wrong value. Double click doesn't have this issue.
        self.tree.bind('<Double-Button-1>', self._select_date)
        # *************************************************************************************************************

        self._initialize_calendar()

    def _initialize_calendar(self):
        current_year = self.date.today().year
        current_month = self.date.today().month  # Current numerical month
        current_written_month = self.date.today().strftime('%B')  # Current month written out

        self.currently_displayed_year.set(current_year)  # Sets label to current year
        self.currently_displayed_month.set(current_written_month)  # Sets label to current month

        # Below returns the first weekday of the month and number of days in the month
        current_month = calendar.monthcalendar(current_year, current_month)
        """
        e.g.
        September 2019
        [0, 0, 0, 0, 0, 0, 1]
        [2, 3, 4, 5, 6, 7, 8]
        [9, 10, 11, 12, 13, 14, 15]
        [16, 17, 18, 19, 20, 21, 22]
        [23, 24, 25, 26, 27, 28, 29]
        [30, 0, 0, 0, 0, 0, 0]
        
        """

        for day in current_month:
            print(day)
            self.tree.insert('', 'end', values=(day))  # INSERTS DATA INTO TREEVIEW


    def _refresh_calendar_month_forward(self, event=None):
        self.tree.delete(*self.tree.get_children())  # Clears treeview days
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])  # Numerical value of month
        year = int(self.year_label.cget('text'))  # Retrieves currently displayed year
        month_forward_value = int(numerical_month) + 1  # Adds one month to current month

        if month_forward_value >= 13:  # Accounts for user advancing year via months aka Dec - Jan
            month_forward_value = 1  # Resets month value to January
            year = year + 1  # Adds one year to reflect advancement
        else:
            pass

        month_forward_calendar = calendar.monthcalendar(year, month_forward_value)  # Builds calendar

        for day in month_forward_calendar:
            self.tree.insert('', 'end', values=(day))  # Inserts data into treeview

        next_written_month = calendar.month_name[month_forward_value]  # Retrieves month name by value
        self.currently_displayed_month.set(next_written_month)  # Sets labels for users
        self.currently_displayed_year.set(year)  # Sets labels for users

    def _refresh_calendar_year_forward(self, event=None):
        pass








    def _select_date(self, event):
        selected_day = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)

        if col == '#1':
            cell_value = selected_day['values'][0]
        elif col == '#2':
            cell_value = selected_day['values'][1]
        elif col == '#3':
            cell_value = selected_day['values'][2]
        elif col == '#4':
            cell_value = selected_day['values'][3]
        elif col == '#5':
            cell_value = selected_day['values'][4]
        elif col == '#6':
            cell_value = selected_day['values'][5]
        elif col == '#7':
            cell_value = selected_day['values'][6]

        print('cell_value = %s' % cell_value)
        """
        The returned output is assembled by using the cget method to retrieve the currently displayed year. Since the 
        month is displayed with the name of the month rather than the numerical value necessary to return a datetime
        object, numerical_month returns the numerical value via the calendar module. It looks up the numerical value
        by month abbreviation, so I splice the month label to the first three letters. The day is the selected_day
        that the user has clicked on. 
        """
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])
        output_date = self.date(int(self.year_label.cget('text')), int(numerical_month), cell_value)
        print(output_date)






"""
TODO:
1) Possibly use global month number and year variable to ensure smooth transition of months and years
2) Figure out how to pull data


"""


