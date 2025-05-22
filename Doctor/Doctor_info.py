from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from matplotlib.dates import DateLocator

from manager import *
from validator import *

window = Tk()
window.title("Doctor Info")
window.geometry("700x400")

#ID
Label(window, text ='ID').place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

#Disease
Label(window, text ='Disease').place(x=20, y=60)
disease = StringVar()
Entry(window, textvariable=disease).place(x=80, y=60)

#Medicine
Label(window, text ='Medicine').place(x=20, y=100)
medicine = StringVar()
Entry(window, textvariable=medicine).place(x=80, y=100)

#Date_visit
Label(window, text='Date of visit').place(x=20, y=150)
date_visit = DateLocator()
Entry(window, textvariable=date_visit).place(x=100, y=150)

window.mainloop()