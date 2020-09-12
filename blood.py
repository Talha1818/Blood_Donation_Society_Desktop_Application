from tkinter import *
import tkinter.messagebox as msg
import Database
import Home
def login(event):
    data=(
        user.get(),
        passw.get()
    )
    if user.get()=="" and passw.get()=="":
        msg.showwarning("username & password!", "Plz set BOTH!!")
    elif user.get() == "":
        msg.showwarning("username!", "plz set Username First!!")
    elif passw.get()=="":
        msg.showwarning("password!", "plz set password First!!")
    else:
        res=Database.user_login(data)
        if res:
            msg.showinfo('Successfully!',"Login Successfully!!")
            root.destroy()
            x=Home.data()
            x.add_frame()
        else:
            msg.showwarning("Error!","Username/Password Incorect!")
            user.set("")
            passw.set("")





root=Tk()
root.geometry("400x300")
root.iconbitmap('blood1.ico')
root.maxsize(400,300)
root.minsize(400,300)
root.title("Login | Blood Donation Society - NTU")
FONT="comicsansms 12 bold"

user=StringVar()
passw=StringVar()


f1=Frame(root)
l1=Label(f1,text="Username", font="courier 14 bold",bg="#ef5151")
l1.grid(row=2,column=1)

e1=Entry(f1,textvariable=user,font="courier 13 bold")
e1.grid(row=2,column=4,ipadx=15,ipady=5)

l2=Label(f1,text="Password", font="courier 14 bold",bg="#ef5151")
l2.grid(row=3,column=1)

e2=Entry(f1,textvariable=passw,show='*',font="courier 13 bold")
e2.grid(row=3,column=4,ipadx=15,pady=5,ipady=5)

b1=Button(f1,text="Login",font="Times 15 bold",borderwidth=3,relief=SUNKEN,bg="#ef5151")
b1.bind('<Button-1>',login)
b1.grid(row=5,column=4,pady=10,ipadx=16,ipady=2)
f1.pack(anchor=NW,padx=70,pady=80)




root.mainloop()