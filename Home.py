from tkinter import *
import tkinter.messagebox as msg
import Database_Insert
import ShowAllDetails
import searchRecords
import pandas as pd
class data:
    def __init__(self, Data='') :
        self.Data = Data
        # print("This is Paramter",self.Data)
        self.window=Tk()
        self.window.geometry("688x500")
        self.window.iconbitmap('blood1.ico')
        self.window.maxsize(688,500)
        self.window.minsize(688,500)
        self.window.title("Blood Donation Society - NTU")

    def add_frame(self):
        self.name = StringVar()
        self.regno = StringVar()
        self.bloodgrp = StringVar()
        self.phone = StringVar()

        self.frame=Frame(self.window)
        self.l_name=Label(self.frame,text="Full Name",font="courier 14 bold",bg="#ef5151")
        self.l_name.grid(row=0,column=1)

        self.l_reg = Label(self.frame, text="Registration No",font="courier 14 bold",bg="#ef5151")
        self.l_reg.grid(row=1, column=1, padx=4)

        self.l_blood_grp = Label(self.frame, text="Blood Group", font="courier 14 bold",bg="#ef5151")
        self.l_blood_grp.grid(row=2, column=1)

        self.l_phone_no = Label(self.frame, text="Phone No", font="courier 14 bold",bg="#ef5151")
        self.l_phone_no.grid(row=3, column=1)

        self.ename=Entry(self.frame,borderwidth=3,relief=SUNKEN, font="courier 13 italic",
                         fg="white",bg="#ef5151",textvariable=self.name)
        self.ename.grid(row=0,column=5,pady=4)

        self.ereg = Entry(self.frame, borderwidth=3, relief=SUNKEN, font="courier 13 italic",
                          fg="white",bg="#ef5151",textvariable=self.regno)
        self.ereg.insert(0,"17-ntu-")
        self.ereg.grid(row=1, column=5,pady=4)

        self.ebg = Entry(self.frame, borderwidth=3, relief=SUNKEN, font="courier 13 italic",
                         fg="white",bg="#ef5151",textvariable=self.bloodgrp)
        self.ebg.grid(row=2, column=5,pady=4)

        self.epn = Entry(self.frame, borderwidth=3, relief=SUNKEN, font="courier 13 italic",
                         fg="white",bg="#ef5151",textvariable=self.phone)

        self.epn.insert(0,"03")
        self.epn.grid(row=3, column=5,pady=4)
        self.frame.pack(anchor=NW,padx=100,pady=60)


        self.frame2 = Frame(self.window)
        # Insert-Button
        if self.Data=='':
            self.btn1 = Button(self.frame2, text="Insert", borderwidth=3, relief=SUNKEN,
                               font="courier 14 bold", bg="#ef5151",command=self.insert)
            # self.btn1.bind('<Button-1>', self.insert)
            self.btn1.pack( pady=4, ipadx=20, ipady=3,side=LEFT)
        else:
            up=dict(self.Data).get('values')
            print(up)
            self.ereg.delete(0,END)
            self.ename.insert(0,up[0])
            self.ereg.insert(0,up[1])
            self.ebg.insert(0,up[2])
            self.epn.insert(0,up[3])
            self.btn1 = Button(self.frame2, text="Update", borderwidth=3, relief=SUNKEN,
                               font="courier 14 bold", bg="#ef5151", command=self.update)
            # self.btn1.bind('<Button-1>', self.insert)
            self.btn1.pack(pady=4, ipadx=20, ipady=3, side=LEFT)

        # ShowAllDeatail-Button
        self.btn2 = Button(self.frame2, text="Show", borderwidth=3, relief=SUNKEN,
                           font="courier 14 bold", bg="#ef5151")
        self.btn2.bind('<Button-1>', self.show)
        self.btn2.pack(pady=4, ipadx=25, ipady=3,side=LEFT,padx=7)

        # SearchDeatails-Button
        self.btn3 = Button(self.frame2, text="Search", borderwidth=3, relief=SUNKEN,
                           font="courier 14 bold", bg="#ef5151")
        self.btn3.bind('<Button-1>', self.search)
        self.btn3.pack(pady=4, ipadx=20, ipady=3, side=LEFT, padx=7)

        self.frame2.pack(anchor=NW,padx=150)

        self.window.mainloop()
    def insert(self):
        data =( self.ename.get(),self.ereg.get(),self.ebg.get(),self.epn.get() )
        self.get_phone = self.phone.get()
        self.get_name = self.name.get()

        if self.name.get()=="" and self.regno.get()=="" and self.bloodgrp.get()=="" and self.phone.get()=="":
            msg.showwarning("Message!","Plz Insert Data!")
        elif self.name.get()=="":
            msg.showwarning("Message!", "Plz Insert Name!")
        elif self.get_name.isdigit():
            msg.showwarning("Message!", "Number Not Allowed in Username!")
        elif len(self.get_name) <= 2:
            msg.showwarning("Message!", "Enter valid Name!")

        elif self.regno.get()=="":
            msg.showwarning("Message!", "Plz Insert Regestration No!")

        elif self.bloodgrp.get()=="":
            msg.showwarning("Message!", "Plz Insert BloodGroup!")
        elif self.bloodgrp.get().isdigit():
            msg.showwarning("Message!", "Enter valid Blood_Group Name!")
        elif self.phone.get()=="":
            msg.showwarning("Message!", "Plz Insert phoneNo!")
        elif len(self.get_phone) < 11 or len(self.get_phone) > 11:
            msg.showwarning("Message!", "Enter valid Phone Number!")

        else:
            if self.phone.get().isdigit():
                res = Database_Insert.user_insert(data)
                if res:
                    msg.showinfo('Successfully!', "Successfully Insert!!")
                    self.ename.delete(0, END)
                    self.ereg.delete(0, END)
                    self.ebg.delete(0, END)
                    self.epn.delete(0, END)
                    self.ereg.insert(0, "17-ntu-")
                    self.epn.insert(0, "03")
                else:
                    msg.showwarning("Error!", "Error!")
            else:
                msg.showwarning("Message!", "Enter valid Phone Number!")



    def update(self):
        x = dict(self.Data).get('values')
        text = x[1]
        # print(text)
        data = (self.ename.get(), self.ereg.get(), self.ebg.get(), self.epn.get(), text)
        # print(data)
        res=Database_Insert.update_details(data)
        # print(res)

        if res:
            msg.showinfo("message","Successfully updated!")
            self.window.destroy()
            z=ShowAllDetails.show()
            z.add_table()

        else:
            msg.showinfo("eroor!","Not updated!")




    def show(self,event):
        self.window.destroy()
        x=ShowAllDetails.show()
        x.add_table()

    def search(self,event):
        self.window.destroy()
        x=searchRecords.Search()
        x.add_fram_search()


if __name__ == '__main__':
    x=data()
    x.add_frame()

