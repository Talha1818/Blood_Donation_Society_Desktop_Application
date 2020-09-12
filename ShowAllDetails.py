from tkinter import *
import tkinter.messagebox as msg
from tkinter.ttk import Treeview, Style
import Database_Insert
import Home
import pandas as pd

class show:
    def __init__(self):
        self.window=Tk()
        self.window.title("Show | All Data | National Textile University Faisalabad")
        self.window.iconbitmap('blood1.ico')
        can=Canvas(self.window,width=800,height=400,bg="white")
        can.pack(expand=YES,fill=BOTH)


        width=self.window.winfo_screenwidth()
        height=self.window.winfo_screenheight()
        # print("Width:",width,"\n","Height:",height)

        x=int(width/2 - 800/2)
        y=int(height/2 - 400/2)
        str1="980x450+"+str(x)+ "+" +str(y)

        self.window.geometry(str1)
        self.window.maxsize(980,450)
        self.window.minsize(980,450)
        # self.window.resizable(width=False,height=False)
    def add_table(self):
        self.frame=Frame(self.window,width=850,height=385,bg="#ef5151")
        self.frame.place(x=77,y=20)

        self.l1=Label(self.frame,text="Students Blood Details",font="Times 20 bold")
        self.l1.place(x=250,y=40)

        # Back-Buton
        self.b1 = Button(self.frame, text="Back", font="Times 12 bold")
        self.b1.place(x=630, y=42)
        self.b1.bind('<Button-1>', self.back)

        # for Style Table
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri 11'))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri 13 bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        # import TreeViewe
        self.tr=Treeview(self.frame,columns=('A','B','C','D','E','F'),selectmode="extended",style='mystyle.Treeview')
        # heading key+text
        self.tr.heading("#0", text="Sr.No")
        self.tr.column("#0", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#1",text="Name")
        self.tr.column("#1",minwidth=0,width=85,stretch=NO)

        self.tr.heading("#2", text="Registration No")
        self.tr.column("#2", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#3", text="Blood Group")
        self.tr.column("#3", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#4", text="Phone No")
        self.tr.column("#4", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#5", text="Update")
        self.tr.column("#5", minwidth=0, width=85, stretch=NO)

        self.tr.heading("#6", text="Delete")
        self.tr.column("#6", minwidth=0, width=85, stretch=NO)

        j=1
        for i in Database_Insert.show_details():
            self.tr.insert('',index=j,text=j,values=(i[0],i[1],i[2],i[3],"update","delete"))
            j+=1

        self.tr.bind('<Double-Button-1>',self.action)

        self.sb = Scrollbar(self.tr)
        self.sb.place(x=580,y=2,height=223,width=20,bordermode=OUTSIDE)
        self.sb.config(command=self.tr.yview)
        self.tr.config(yscrollcommand=self.sb.set)


        self.tr.place(x=85,y=85)

        self.b1 = Button(self.frame, text="Save Excel", font="Times 14 bold",bg="#ef5151",borderwidth=3,
        relief=RIDGE)
        self.b1.place(x=320, y=320)
        self.b1.bind('<Button-1>', self.excel)


        self.window.mainloop()
    def action(self,event):
        fcs=self.tr.focus()
        col=self.tr.identify_column(event.x)
        x=self.tr.item(fcs).get('values')
        text=x[1]
        data=(
            text,
        )
        if col=="#6":
            res=msg.askyesno("Message!","Do you want to delete?")
            if res:
                d=Database_Insert.delete_details(data)
                if d:
                    msg.showinfo("Deleted","Successfully")
                    self.window.destroy()
                    x=show()
                    x.add_table()
                else:
                    self.window.destroy()
                    x=show()
                    x.add_table()
        elif col=="#5":
            # self.window.destroy()
            x=Home.data(self.tr.item(fcs))
            x.add_frame()

    def back(self,event):
        self.window.destroy()
        x=Home.data()
        x.add_frame()
    def excel(self,event):
        try:
            x=Database_Insert.show_details()
            name=[]
            regno=[]
            bg=[]
            phone=[]
            for i in range(len(x)):
                z=x.__getitem__(i)
                name.append(z[0])
                regno.append(z[1])
                bg.append(z[2])
                phone.append(z[3])



            student = pd.DataFrame({
                "Name": name,
                "Reg_No":regno,
                "Blood_G":bg,
                "Phone_No":phone
            })

            with pd.ExcelWriter("BDS_NTU.xlsx") as writer:
                student.to_excel(writer, sheet_name="BDS_Student", index=False)
            msg.showinfo("Message!", "Susccessfully Insert!")
        except:
            msg.showwarning("Message!","Something Went Wrong!")


if __name__ == '__main__':
    x=show()
    x.add_table()