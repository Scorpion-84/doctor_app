from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


from manager import *
from validator import *

ills_list = read_from_file("persons.dat")

def load_data(ills_list):
    ills_list = read_from_file("persons.dat")
    for row in table.get_children():
        table.delete(row)

    for ill in ills_list:
        table.insert("", END, values=ill)


def reset_form():
    id.set(len(ills_list) + 1)
    disease.set("")
    medicine.set("")
    date_visit.set(0)
    name_doctor.set("")
    load_data(ills_list)

def save_btn_click():
    person = (id.get(), disease.get(), medicine.get(), date_visit.get(), name_doctor.get())
    errors = ills_validator(ill)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        ills_list.append(person)
        write_to_file("persons.dat", ills_list)
        reset_form()

def table_select(x):
    selected_person = table.item(table.focus())["values"]
    if selected_person:
        id.set(selected_person[0])
        disease.set(selected_person[1])
        medicine.set(selected_person[2])
        date_visit.set(selected_person[3])
        name_doctor.set(selected_person[4])

def edit_btn_click():
    pass


def remove_btn_click():
    pass


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
date_visit = DateTime()
Entry(window, textvariable=date_visit).place(x=110, y=150)

#Name_doctor
Label(window, text="Name's doctor").place(x=20, y=200)
name_doctor = StringVar()
Entry(window, textvariable=name_doctor).place(x=110, y=200)

table = ttk.Treeview(window, columns=[1, 2, 3, 4], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Account")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=250, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=290)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=290)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=290)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=240, width=190)


window.mainloop()