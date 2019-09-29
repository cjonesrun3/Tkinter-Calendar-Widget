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
        self.year_forward_button = ttk.Button(self.year_frame, style='R.TButton',
                                              command=self._refresh_calendar_year_forward)
        self.year_back_button = ttk.Button(self.year_frame, style='L.TButton',
                                           command=self._refresh_calendar_year_back)

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
        self.month_back_button = ttk.Button(self.month_frame, style='L.TButton',
                                            command=self._refresh_calendar_month_back)

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
                self.tree.insert('', 'end', values=(day), tag='FirstWeek')  # Inserts data into treeview
            else:
                self.tree.insert('', 'end', values=(day))  # Inserts data into treeview


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
            self.tree.insert('', 'end', values=(day))  # Inserts data into treeview

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
            self.tree.insert('', 'end', values=(day))  # Inserts data into treeview

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
        if numerical_month - 1 == 0:  # Checks to ensure previous month isn't in previous year
            previous_month_amount_of_days = calendar.monthrange(year - 1, 12)[1]
            # Subtracts one from year, set month to December and returns only days
        else:
            previous_month_amount_of_days = calendar.monthrange(year, month_back_value - 1)[1]
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
            self.tree.insert('', 'end', values=(day))  # Inserts data into treeview

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
            self.tree.insert('', 'end', values=(day))

        self.currently_displayed_year.set(year_back_value)


    def _select_date(self, event):
        selected_day = self.tree.item(self.tree.focus())  # Item clicked
        col = self.tree.identify_column(event.x)  # North/South columns returns data from entire row
        row = self.tree.identify_row(event.y)
        print(selected_day.items())


        # variable and changed based on selection. Otherwise, you can select a date from the previous month, but
        # It will return a datetime with the month the user is currently on
        numerical_month = list(calendar.month_abbr).index(self.month_label.cget('text')[:3])
        numerical_year = int(self.year_label.cget('text'))

        month_of_date_selected = 0  # Initializing as current displayed month
        year_of_date_selected = 0  # Initializing as current displayed year

        if col == '#1':
            print('column 1')
            if selected_day['tags'][0] == 'FirstWeek':  # Checks first row for numbers from previous month
                print('This is a first row variabl')
                if selected_day['values'][0] > 7:
                    month_of_date_selected = numerical_month - 1
                    print('modifying')
                    print(month_of_date_selected)
            elif row == 'I006':  # Checks last row for number in next month
                if selected_day['values'][0] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][0]


        elif col == '#2':
            if row == 'I001':
                if selected_day['values'][1] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][1] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][1]

        elif col == '#3':
            if row == 'I001':
                if selected_day['values'][2] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][2] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][2]

        elif col == '#4':
            if row == 'I001':
                if selected_day['values'][3] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][3] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][3]


        elif col == '#5':
            if row == 'I001':
                if selected_day['values'][4] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][4] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][4]

        elif col == '#6':
            if row == 'I001':
                if selected_day['values'][5] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][5] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][5]

        elif col == '#7':
            if row == 'I001':
                if selected_day['values'][6] > 7:
                    month_of_date_selected = numerical_month - 1
            elif row == 'I006':
                if selected_day['values'][6] < 7:
                    month_of_date_selected = numerical_month + 1
            cell_value = selected_day['values'][6]

        print('cell_value = %s' % cell_value)
        """
        The returned output is assembled by using the cget method to retrieve the currently displayed year. Since the 
        month is displayed with the name of the month rather than the numerical value necessary to return a datetime
        object, numerical_month returns the numerical value via the calendar module. It looks up the numerical value
        by month abbreviation, so I splice the month label to the first three letters. The day is the selected_day
        that the user has clicked on. 
        """
        print(month_of_date_selected)
        print(year_of_date_selected)

        if month_of_date_selected == 0:
            month_of_date_selected = numerical_month
        if year_of_date_selected == 0:
            year_of_date_selected = numerical_year
        output_date = self.date(year_of_date_selected, month_of_date_selected, cell_value)
        print(output_date)
        # TODO Figure out return






"""
TODO:
1) Possibly use global month number and year variable to ensure smooth transition of months and years
2) Figure out how to pull data


"""


