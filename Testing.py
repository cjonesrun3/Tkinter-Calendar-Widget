import TCalendar
import tkinter as tk
from tkinter import ttk

from TCalendar import TreeCalendar

root = tk.Tk()
a = TreeCalendar(root, background='red', foreground='red')
a.pack()
b = ttk.Button(root, text='BUUTAN')
b.pack()
root.mainloop()

