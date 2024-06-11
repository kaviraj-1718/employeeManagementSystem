
#import tkinter for creating GUI
from tkinter import *
from tkinter import ttk ##ttk is used to create additional themes
from tkinter import messagebox #messagebox is used to display alert boxes
from db import Database #database is imported 

db = Database("Employee.db")  #connecting the database
root = Tk()   #creating root or main window of GUI
root.title("Employee Management System") #adding title
root.geometry("1920x1080+0+0") #1920x1080 - size of the window; 0+0 -  window starts at top left corner
root.config(bg="#2c3e50") #setting bg color of root/main window
root.state("zoomed") #Maximizes the window to occupy the entire screen by setting its state to "zoomed".


#StringVar()  is a variable class used to create a special variable linked to widget attributes
name = StringVar() # Any changes to this variable will reflect in the connected widgets.
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame

entries_frame = Frame(root, bg="#535c68") #This line initializes a Frame widget(frames are different parts of a GUI). It is within the root.
entries_frame.pack(side=TOP, fill=X) #This packs the entries_frame at the top (side=TOP) of the root window; fille=X (makes this frame occupy the full window)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white") #create a Label widget named title inside the entries_frame
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

#creating frames and grid(similar to table) for all the fields such as name, age,....

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus() #This retrieves the currently focused or selected row in the TreeView widget (tv), when the function is called.
                                #The focus() method is commonly used to determine the currently selected item in tkinter.
    data = tv.item(selected_row) #It obtains all the details associated with the selected row using the item method
    global row #This line declares a global variable named row.
    row = data["values"] #It assigns the values of the selected row to the row variable. it is a tuple.
    #print(row)
    name.set(row[1]) #Sets the name variable (StringVar) to the value from the second element of row
    age.set(row[2]) #Sets the age variable (StringVar) to the value from the third element of row
    doj.set(row[3]) #Sets the doj variable (StringVar) to the value from the fourth element of row
    email.set(row[4]) #Sets the email variable (StringVar) to the value from the fifth element of row
    gender.set(row[5]) #Sets the gender variable (StringVar) to the value from the sixth element of row
    contact.set(row[6]) #Sets the contact variable (StringVar) to the value from the seventh element of row
    txtAddress.delete(1.0, END) #Clears the content of a txtAddress widget.
    txtAddress.insert(END, row[7]) # Inserts the content of the eighth element of row into the txtAddress widget

def dispalyAll():
    tv.delete(*tv.get_children()) # Clears any existing items in the TreeView widget (tv)
    for row in db.fetch(): #This initiates a loop that fetches rows of data from the database using the fetch() method
        tv.insert("", END, values=row) #display all records in the TreeView widget as rows, each row containing data from the database.


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return #if any of the fields are unfilled/ empty, it displays an error message. "" is used to denote empty field.
    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
            1.0, END)) #gets all the input values using get() method.
    messagebox.showinfo("Success", "Record Inserted") 
    clearAll() #clears the input fields
    dispalyAll() #calls display function to display all the details



def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END)) #get the newly entered values
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0]) #row 0  refers to the unique id of each employee. Removing that will delete the entire employee.
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)

#buttons for submit,delete,update and clear.
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=600)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50) 
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=50, anchor="center")
tv.heading("2", text="Name")
tv.column("2", width=5, anchor="center")
tv.heading("3", text="Age")
tv.column("3", width=5, anchor="center")
tv.heading("4", text="D.O.B")
tv.column("4", width=10, anchor="center")
tv.heading("5", text="Email")
tv.column("5", width=5, anchor="center")
tv.heading("6", text="Gender")
tv.column("6", width=10, anchor="center")
tv.heading("7", text="Contact")
tv.column("7", width=20, anchor="center")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()