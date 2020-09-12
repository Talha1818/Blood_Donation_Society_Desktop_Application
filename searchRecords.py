from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
import Database_Insert
import ShowAllDetails
import Home
import tkinter.messagebox as msg

class Search:
    def __init__(self):
        self.window = Tk()
        self.window.title("Search | All Record | National Textile University Faisalabad")
        self.window.iconbitmap('blood1.ico')
        can = Canvas(self.window, width=800, height=400, bg="white")
        can.pack(expand=YES, fill=BOTH)

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        # print("Width:",width,"\n","Height:",height)

        x = int(width / 2 - 800 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "980x450+" + str(x) + "+" + str(y)

        self.window.geometry(str1)
        self.window.maxsize(980,450)
        self.window.minsize(980,450)

    def add_fram_search(self):
        self.frame = Frame(self.window, width=850,height=385, bg="#ef5151")
        self.frame.place(x=77, y=20)

        self.l1 = Label(self.frame, text="Enter Reg_N/Blood_G:", font="Times 16 bold")
        self.l1.place(x=50, y=43)

        self.Entry_reg=Entry(self.frame, font="courior 14 bold")
        self.Entry_reg.place(x=280,y=43,height=30)

        # search-Button
        self.b1 = Button(self.frame, text="Search-RN", font="Times 12 bold")
        self.b1.place(x=510, y=40, height=37)
        self.b1.bind('<Button-1>', self.regno)

        self.b1 = Button(self.frame, text="Search-BG", font="Times 12 bold")
        self.b1.place(x=599, y=40, height=37)
        self.b1.bind('<Button-1>', self.bg)


        # Back-Buton
        self.b1 = Button(self.frame, text="Back", font="Times 12 bold")
        self.b1.place(x=690, y=40,height=37)
        self.b1.bind('<Button-1>', self.back)

     # for Styling Table
        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri 11'))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri 13 bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders


        # import TreeViewe
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D','E','F'), selectmode="extended",style="mystyle.Treeview")
        # heading key+text

        self.tr.heading("#0", text="Sr_No")
        self.tr.column("#0", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#1", text="Name")
        self.tr.column("#1", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#2", text="Reg_No")
        self.tr.column("#2", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#3", text="Blood_Group")
        self.tr.column("#3", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#4", text="Phone_No")
        self.tr.column("#4", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#5", text="update")
        self.tr.column("#5", minwidth=0, width=100, stretch=NO)

        self.tr.heading("#6", text="delete")
        self.tr.column("#6", minwidth=0, width=100, stretch=NO)



        self.sb = Scrollbar(self.tr)
        self.sb.place(x=673, y=2, height=223, width=20, bordermode=OUTSIDE)
        self.sb.config(command=self.tr.yview)
        self.tr.config(yscrollcommand=self.sb.set)

        self.tr.place(x=50, y=100,width=691)
# Remove All ROW
        self.Entry_reg.bind('<KeyRelease>', self.remove)

        self.tr.bind('<Double-Button-1>', self.action)






        self.window.mainloop()

    def regno(self,event):
        try:
            data = (
                self.Entry_reg.get(),

            )
            if self.Entry_reg.get()=="":
                msg.showwarning("Message!","insert Reg No!")
            else:
                j = 1
                D=Database_Insert.search_details(data)
                if D:
                    self.Entry_reg.delete(0,END)
                    for i in D:
                        self.tr.insert('', index=j, text=j, values=(i[0],i[1], i[2], i[3],"update","delete"))
                        j+=1
                else:
                    msg.showwarning("Message!", "No result Found!")

        except:
            msg.showwarning("Error!","ERORR!")


    def bg(self,event):
        try:
            data = (
                self.Entry_reg.get(),

            )
            if self.Entry_reg.get()=="":
                msg.showwarning("Message!","insert Blood_Group!")
            else:
                j = 1
                D=Database_Insert.search_details_bg(data)
                if D:
                    self.Entry_reg.delete(0,END)
                    for i in D:
                        self.tr.insert('', index=j, text=j, values=(i[0],i[1], i[2], i[3],"update","delete"))
                        j+=1
                else:
                    msg.showwarning("Message!", "No result Found!")

        except:
            msg.showwarning("Error!","ERORR!")


    def remove(self,event):
        x = self.tr.get_children()
        if x != '()':
            for child in x:
                self.tr.delete(child)

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
                    x=Search()
                    x.add_fram_search()
                else:
                    self.window.destroy()
                    x = Search()
                    x.add_fram_search()
        elif col=="#5":
            # self.window.destroy()
            x=Home.data(self.tr.item(fcs))
            x.add_frame()


    def back(self, event):
        self.window.destroy()
        x = Home.data()
        x.add_frame()

if __name__ == '__main__':
    x=Search()
    x.add_fram_search()