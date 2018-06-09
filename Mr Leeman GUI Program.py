from tkinter import *

gui = Tk()
gui.title("Mr Leeman's Child Information System")
Label(gui, text="Username").grid(row=0)
Label(gui, text="Password").grid(row=1)

username = Entry(gui)
password = Entry(gui)

username.grid(row=0, column=1)
password.grid(row=1, column=1)

Button(gui, text='Enter').grid(row=3, column=0, sticky=W, pady=4)

mainloop( )

if username == "admin" and password == "pass":
    Label(gui, text="Child Information").grid(row=2)
    Label(gui, text="Forename").grid(row=1)
    Label(gui, text="Surname").grid(row=2)

    childfore = Entry(gui)
    childsur = Entry(gui)

    childfore.grid(row=1, column=1)
    childsur.grid(row=2, column=1)
else:
    messagebox.showinfo("ERROR", "You're an Invalid.")
