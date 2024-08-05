import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("Student Details")

form_frame=ttk.Frame(root,padding=20)
form_frame.grid()

name_label=ttk.Label(form_frame,text="Name:")
name_label.grid(column=0,row=0,sticky=tk.W)
name_entry=ttk.Entry(form_frame)
name_entry.grid(column=1,row=0)

id_label=ttk.Label(form_frame,text="ID:")
id_label.grid(column=0,row=1,sticky=tk.W)
id_entry=ttk.Entry(form_frame)
id_entry.grid(column=1,row=1)

class_label=ttk.Label(form_frame,text="Class:")
class_label.grid(column=0,row=2,sticky=tk.W)
class_entry=ttk.Entry(form_frame)
class_entry.grid(column=1,row=2)

contact_label=ttk.Label(form_frame,text="Contact:")
contact_label.grid(column=0,row=3,sticky=tk.W)
contact_entry=ttk.Entry(form_frame)
contact_entry.grid(column=1,row=3)

remarks_label=ttk.Label(form_frame,text="Remarks:")
remarks_label.grid(column=0,row=4,sticky=tk.W)
remarks_entry=ttk.Entry(form_frame)
remarks_entry.grid(column=1,row=4)

submit_button=ttk.Button(form_frame,text="Submit")
submit_button.grid(column=1,row=5)

def submit_form():
	name=name_entry.get()
	id_=id_entry.get()
	class_=class_entry.get()
	contact=contact_entry.get()
	remarks=remarks_entry.get()
	print(f"Name:{name}, ID:{id_}, Class:{class_}, Contact:{contact}, Remarks:{remarks}")
	name_entry.delete(0,tk.END)
	id_entry.delete(0,tk.END)
	class_entry.delete(0,tk.END)
	contact_entry.delete(0,tk.END)
	remarks_entry.delete(0,tk.END)
	
	name_entry.focus()
submit_button.config(command=submit_form)
root.mainloop()
