# !Python3
# 29SEP2019
# BY: C.R. JONES
# PYTHON VERSION 3.6.1

"""
This is a simple calendar widget using the treeview widget as the calendar. It returns a datetime object when a user
clicks on a date.


"""

import calendar
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    import ttk
    from tkinter import *


class TreeCalendar(ttk.Frame):
    date = calendar.datetime.date
    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta
    strptime = calendar.datetime.datetime.strptime

    def __init__(self, master=None, **kw):
        """
        Start of widget

        ________________________________________________
                        self.year_frame
                        self.month_frame
                        self.tree_frame

        Configuration Options:

        Option                                                                      Accepts Data type
        background - Will change background for buttons, frames, and treeview               Str
        foreground - Arrow colors, treeview text headers, dates                             Str
        activebackground -                                                                  Str
        fieldbackground - Treeview fluctuates number of rows. When there's less,
        this color will show                                                                Str
        font - Year and month label                                                         Str
        fontsize - Calendar dates, Year label, month label                                  int or Str
        calendarcolumnwidth - Calendar columns width                                        int or Str
        calendarheight - Height of the calendar                                             int or Str
        arrowsize - Size of arrors on buttons                                               int or Str
        """

        ttk.Frame.__init__(self, master)  # Base frame
        self.style = ttk.Style(self)
        self._style_prefixe = str(self)  # Ensures styles are unique to individual calendars
        ttk.Frame.configure(self, style='main.%s.TFrame' % self._style_prefixe)
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

        self.style.layout('L.%s.TButton' % self._style_prefixe,
                          [('Button.focus',
                            {'children': [('Button.leftarrow', None)]})])
        self.style.layout('R.%s.TButton' % self._style_prefixe,
                          [('Button.focus',
                            {'children': [('Button.rightarrow', None)]})])

        self.style.configure('R.%s.TButton' % self._style_prefixe, background=selected_background,
                             arrowcolor=selected_foreground, bordercolor=selected_background,
                             relief="flat", lightcolor=selected_background, darkcolor=selected_background,
                             arrowsize=int(selected_arrowsize))

        self.style.configure('L.%s.TButton' % self._style_prefixe, background=selected_background,
                             arrowcolor=selected_foreground, bordercolor=selected_background, relief="flat",
                             lightcolor=selected_background, darkcolor=selected_background,
                             arrowsize=int(selected_arrowsize))

        self.style.configure('%s.TFrame' % self._style_prefixe, background=selected_background)

        self.style.layout('Cal.%s.Treeview' % self._style_prefixe)
        # Unique designation to avoid interfering with other treeviews

        self.style.configure('Cal.%s.Treeview' % self._style_prefixe, background=selected_background, relief='raised',
                             foreground=selected_foreground, activebackground=selected_activebackground,
                             fieldbackground=selected_fieldbackground, font=(selected_font, int(selected_fontsize)))

        self.style.configure('Cal.%s.Treeview.Heading' % self._style_prefixe, foreground=selected_foreground,
                             background=selected_background, activebackground=selected_activebackground,
                             font=(selected_font, int(selected_fontsize)))

        self.style.configure('%s.TLabel' % self._style_prefixe, background=selected_background,
                             font=(selected_font, int(selected_fontsize)))

        # *************************************************************************************************************
        # self.year_frame
        # *************************************************************************************************************
        self.year_frame = ttk.Frame(self)
        self.year_frame.configure(style='%s.TFrame' % self._style_prefixe)
        self.year_label = ttk.Label(self.year_frame, textvariable=self.currently_displayed_year,
                                    style='%s.TLabel' % self._style_prefixe)
        self.year_forward_button = ttk.Button(self.year_frame, style='R.%s.TButton' % self._style_prefixe,
                                              command=self._refresh_calendar_year_forward)
        self.year_back_button = ttk.Button(self.year_frame, style='L.%s.TButton' % self._style_prefixe,
                                           command=self._refresh_calendar_year_back)

        self.year_back_button.grid(column=0, row=0)
        self.year_label.grid(column=1, row=0)
        self.year_forward_button.grid(column=2, row=0)

        # *************************************************************************************************************
        # self.month_frame
        # *************************************************************************************************************
        self.month_frame = ttk.Frame(self)
        self.month_frame.configure(style='%s.TFrame' % self._style_prefixe)
        self.month_label = ttk.Label(self.month_frame, textvariable=self.currently_displayed_month,
                                     style='%s.TLabel' % self._style_prefixe)
        self.month_forward_button = ttk.Button(self.month_frame, style='R.%s.TButton' % self._style_prefixe,
                                               command=self._refresh_calendar_month_forward)
        self.month_back_button = ttk.Button(self.month_frame, style='L.%s.TButton' % self._style_prefixe,
                                            command=self._refresh_calendar_month_back)

        self.month_back_button.grid(column=0, row=0)
        self.month_label.grid(column=1, row=0)
        self.month_forward_button.grid(column=2, row=0)
        # *************************************************************************************************************
        # self.tree_frame
        # *************************************************************************************************************
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.configure(style='%s.TFrame' % self._style_prefixe)

        self.tree_headers = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

        self.tree = ttk.Treeview(self.tree_frame, columns=self.tree_headers,
                                 style='Cal.%s.Treeview' % self._style_prefixe)

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
        # Using single click as a binding generally raises index errors and results in the current selection being
        # In the same column, but often the wrong value. Double click doesn't have this issue.
        self.tree.bind('<ButtonRelease-1>', self._select_date)  # Double
        # *************************************************************************************************************

        self._initialize_calendar()

    def _initialize_calendar(self):
        """
        Initializes the calendar portion of the widget. Default is to set to current month and year

        """
        current_year = self.date.today().year
        current_month = self.date.today().month  # Current numerical month
        current_written_month = self.date.today().strftime('%B')  # Current month written out

        self.currently_displayed_year.set(current_year)  # Sets label to current year
        self.currently_displayed_month.set(current_written_month)  # Sets label to current month

        # Below returns the first weekday of the month and number of days in the month
        current_month_calendar = calendar.monthcalendar(current_year, current_month)
        """
        e.g. of what current_month returns for September 2019:
        
        [0, 0, 0, 0, 0, 0, 1]
        [2, 3, 4, 5, 6, 7, 8]
        [9, 10, 11, 12, 13, 14, 15]
        [16, 17, 18, 19, 20, 21, 22]
        [23, 24, 25, 26, 27, 28, 29]
        [30, 0, 0, 0, 0, 0, 0]
        
        Below begins the process of replacing 0's with previous and next months days
        """
        previous_month_amount_of_days = 0  # Amount of days in previous month
        if current_month - 1 == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(current_year - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(current_year, current_month - 1)[1]
            # Returns days in previous month

        number_of_zero_slots_for_beggining_of_month = current_month_calendar[0].count(0)  # See below
        # Above counts 0's which allows us to know how many slots in the current month will need to be filled by
        # Previous dates
        for (i, item) in enumerate(current_month_calendar[0]):
            if item == 0:
                current_month_calendar[0][i] = (previous_month_amount_of_days -
                                                number_of_zero_slots_for_beggining_of_month) + (i + 1)

        beggining_of_next_month_days = 1  # Starts next month at one and adds 1 until 0's are gone
        for (i, item) in enumerate(current_month_calendar[-1]):  # Use -1 to always get last list in current_month_cal.
            if item == 0:
                current_month_calendar[-1][i] = beggining_of_next_month_days
                beggining_of_next_month_days += 1

        for day in current_month_calendar:
            if day == current_month_calendar[0]:
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Adds tag for _select_date function
            elif day == current_month_calendar[-1]:
                self.tree.insert('', 'end', values=(day), tag='LastWeek')  # Adds tag for _select_date function
            else:
                self.tree.insert('', 'end', values=(day), tag='CentralWeek')  # Inserts data into treeview

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

        previous_month_amount_of_days = 0  # Amount of days in previous month
        if month_forward_value - 1 == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(year - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(year, month_forward_value - 1)[1]
            # Returns days in previous month

        number_of_zero_slots_for_beggining_of_month = month_forward_calendar[0].count(0)  # See below
        # Above counts 0's which allows us to know how many slots in the current month will need to be filled by
        # Previous dates
        for (i, item) in enumerate(month_forward_calendar[0]):
            if item == 0:
                month_forward_calendar[0][i] = (previous_month_amount_of_days -
                                                number_of_zero_slots_for_beggining_of_month) + (i + 1)

        beggining_of_next_month_days = 1  # Starts next month at one and adds 1 until 0's are gone
        for (i, item) in enumerate(month_forward_calendar[-1]):  # Use -1 to always get last list in current_month_cal.
            if item == 0:
                month_forward_calendar[-1][i] = beggining_of_next_month_days
                beggining_of_next_month_days += 1

        for day in month_forward_calendar:
            if day == month_forward_calendar[0]:
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Adds tag for _select_date function
            elif day == month_forward_calendar[-1]:
                self.tree.insert('', 'end', values=(day), tag='LastWeek')  # Adds tag for _select_date_function
            else:
                self.tree.insert('', 'end', values=(day), tag='CentralWeek')  # Inserts data into treeview

        next_written_month = calendar.month_name[month_forward_value]  # Retrieves month name by value
        self.currently_displayed_month.set(next_written_month)  # Sets labels for users
        self.currently_displayed_year.set(year)  # Sets labels for users

    def _refresh_calendar_year_forward(self, event=None):
        self.tree.delete(*self.tree.get_children())
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])  # Numerical value of month
        year_forward_value = int(self.year_label.cget('text')) + 1  # Adds one to year

        year_forward_calendar = calendar.monthcalendar(year_forward_value, numerical_month)  # Builds calendar

        previous_month_amount_of_days = 0  # Amount of days in previous month
        if numerical_month - 1 == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(year_forward_value - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(year_forward_value, numerical_month - 1)[1]
            # Returns days in previous month

        number_of_zero_slots_for_beggining_of_month = year_forward_calendar[0].count(0)  # See below
        # Above counts 0's which allows us to know how many slots in the current month will need to be filled by
        # Previous dates
        for (i, item) in enumerate(year_forward_calendar[0]):
            if item == 0:
                year_forward_calendar[0][i] = (previous_month_amount_of_days -
                                                number_of_zero_slots_for_beggining_of_month) + (i + 1)

        beggining_of_next_month_days = 1  # Starts next month at one and adds 1 until 0's are gone
        for (i, item) in enumerate(year_forward_calendar[-1]):  # Use -1 to always get last list in current_month_cal.
            if item == 0:
                year_forward_calendar[-1][i] = beggining_of_next_month_days
                beggining_of_next_month_days += 1

        for day in year_forward_calendar:
            if day == year_forward_calendar[0]:
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Inserts data into treeview
            elif day == year_forward_calendar[-1]:
                self.tree.insert('', 'end', values=(day), tag='LastWeek')
            else:
                self.tree.insert('', 'end', values=(day), tag='CentralWeek')  # Inserts data into treeview

        self.currently_displayed_year.set(year_forward_value)  # Sets label to year + 1

    def _refresh_calendar_month_back(self, event=None):
        self.tree.delete(*self.tree.get_children())
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])  # Numerical value of month
        year = int(self.year_label.cget('text'))  # Retrieves currently displayed year
        month_back_value = int(numerical_month) - 1  # Subtracts one month to current month

        if month_back_value == 0:  # Accounts for moving back year via months
            month_back_value = 12  # Sets month to december
            year = year - 1  # Sets year back one
        else:
            pass

        month_back_calendar = calendar.monthcalendar(year, month_back_value)  # Builds calendar for month back

        previous_month_amount_of_days = 0  # Amount of days in previous month
        if numerical_month == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(year - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(year, month_back_value)[1]
            # Returns days in previous month

        number_of_zero_slots_for_beggining_of_month = month_back_calendar[0].count(0)  # See below
        # Above counts 0's which allows us to know how many slots in the current month will need to be filled by
        # Previous dates
        for (i, item) in enumerate(month_back_calendar[0]):
            if item == 0:
                month_back_calendar[0][i] = (previous_month_amount_of_days -
                                               number_of_zero_slots_for_beggining_of_month) + (i + 1)

        beggining_of_next_month_days = 1  # Starts next month at one and adds 1 until 0's are gone
        for (i, item) in enumerate(month_back_calendar[-1]):  # Use -1 to always get last list in current_month_cal.
            if item == 0:
                month_back_calendar[-1][i] = beggining_of_next_month_days
                beggining_of_next_month_days += 1

        for day in month_back_calendar:
            if day == month_back_calendar[0]:
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Inserts data into treeview
            elif day == month_back_calendar[-1]:
                self.tree.insert('', 'end', values=(day), tag='LastWeek')
            else:
                self.tree.insert('', 'end', values=(day), tag='CentralWeek')  # Inserts data into treeview

        previous_written_month = calendar.month_name[month_back_value]  # Retrieves month name by value
        self.currently_displayed_year.set(year)  # Sets label to year
        self.currently_displayed_month.set(previous_written_month)  # Sets label to month

    def _refresh_calendar_year_back(self, event=None):
        self.tree.delete(*self.tree.get_children())  # Clears treeview
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])  # Numerical value of month
        year_back_value = int(self.year_label.cget('text')) - 1  # Subtracts year from current year

        year_back_calendar = calendar.monthcalendar(year_back_value, numerical_month)  # Builds calendar

        previous_month_amount_of_days = 0  # Amount of days in previous month
        if numerical_month - 1 == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(year_back_value - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(year_back_value, numerical_month - 1)[1]
            # Returns days in previous month

        number_of_zero_slots_for_beggining_of_month = year_back_calendar[0].count(0)  # See below
        # Above counts 0's which allows us to know how many slots in the current month will need to be filled by
        # Previous dates
        for (i, item) in enumerate(year_back_calendar[0]):
            if item == 0:
                year_back_calendar[0][i] = (previous_month_amount_of_days -
                                               number_of_zero_slots_for_beggining_of_month) + (i + 1)

        beggining_of_next_month_days = 1  # Starts next month at one and adds 1 until 0's are gone
        for (i, item) in enumerate(year_back_calendar[-1]):  # Use -1 to always get last list in current_month_cal.
            if item == 0:
                year_back_calendar[-1][i] = beggining_of_next_month_days
                beggining_of_next_month_days += 1

        for day in year_back_calendar:
            if day == year_back_calendar[0]:
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Inserts data into treeview
            elif day == year_back_calendar[-1]:
                self.tree.insert('', 'end', values=(day), tag='LastWeek')
            else:
                self.tree.insert('', 'end', values=(day), tag='CentralWeek')  # Inserts data into treeview

        self.currently_displayed_year.set(year_back_value)

    def _select_date(self, event):
        selected_day = self.tree.item(self.tree.focus())  # Item clicked
        col = self.tree.identify_column(event.x)  # North/South columns returns data from entire row

        # variable and changed based on selection. Otherwise, you can select a date from the previous month, but
        # It will return a datetime with the month the user is currently on
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])
        numerical_year = int(self.year_label.cget('text'))

        cell_value = ''  # Str value for clicked on cell

        if col == '#1':  # Columns run North/South on treeview each column is called out individually
            if selected_day['tags'][0] == 'FirstWeek':  # Checks first row for numbers from previous month via tag
                if selected_day['values'][0] > 7:
                    numerical_month = numerical_month - 1

            elif selected_day['tags'][0] == 'LastWeek':  # Checks last row for number in next month via tag
                if selected_day['values'][0] < 7:
                    numerical_month = numerical_month + 1

            cell_value = selected_day['values'][0]

        elif col == '#2':
            if selected_day['tags'][0] == 'FirstWeek':
                if selected_day['values'][1] > 7:
                    numerical_month = numerical_month - 1
            elif selected_day['tags'][0] == 'LastWeek':
                if selected_day['values'][1] < 7:
                    numerical_month = numerical_month + 1
            cell_value = selected_day['values'][1]

        elif col == '#3':
            if selected_day['tags'][0] == 'FirstWeek':
                if selected_day['values'][2] > 7:
                    numerical_month = numerical_month - 1
            elif selected_day['tags'][0] == 'LastWeek':
                if selected_day['values'][2] < 7:
                    numerical_month = numerical_month + 1
            cell_value = selected_day['values'][2]

        elif col == '#4':
            if selected_day['tags'][0] == 'FirstWeek':
                if selected_day['values'][3] > 7:
                    numerical_month = numerical_month - 1
            elif selected_day['tags'][0] == 'LastWeek':
                if selected_day['values'][3] < 7:
                    numerical_month = numerical_month + 1
            cell_value = selected_day['values'][3]

        elif col == '#5':
            if selected_day['tags'][0] == 'FirstWeek':
                if selected_day['values'][4] > 7:
                    numerical_month = numerical_month - 1
            elif selected_day['tags'][0] == 'LastWeek':
                if selected_day['values'][4] < 7:
                    numerical_month = numerical_month + 1
            cell_value = selected_day['values'][4]

        elif col == '#6':
            if selected_day['tags'][0] == 'FirstWeek':
                if selected_day['values'][5] > 7:
                    numerical_month = numerical_month - 1
            elif selected_day['tags'][0] == 'LastWeek':
                if selected_day['values'][5] < 7:
                    numerical_month = numerical_month + 1
            cell_value = selected_day['values'][5]

        elif col == '#7':  # Column 7 has try/except for extra column that will occur in months with less columns
            try:
                if selected_day['tags'][0] == 'FirstWeek':
                    if selected_day['values'][6] > 7:
                        numerical_month = numerical_month - 1
                elif selected_day['tags'][0] == 'LastWeek':
                    if selected_day['values'][6] < 7:
                        numerical_month = numerical_month + 1
                cell_value = selected_day['values'][6]
            except IndexError:
                pass

        """
        The returned output is assembled by using the cget method to retrieve the currently displayed year. Since the 
        month is displayed with the name of the month rather than the numerical value necessary to return a datetime
        object, numerical_month returns the numerical value via the calendar module. It looks up the numerical value
        by month abbreviation, so I splice the month label to the first three letters. The day is the selected_day
        that the user has clicked on. 
        """
        if numerical_month == 13:  # This catches transitions in year. This would catch clicking a date 1 year ahead
            numerical_year = numerical_year + 1
            numerical_month = 1

        if numerical_month == 0:  # This catches clicking a date that's a year back
            numerical_year = numerical_year - 1
            numerical_month = 12

        try:
            self._output_date = self.date(numerical_year, numerical_month, cell_value)

        except TypeError:
            pass


    def send_selected(self):
        """
        Returns datetime object back to user

        """
        try:
            return self._output_date

        except AttributeError:
            pass


"""


"""


