from tkinter import *
from tkinter import messagebox as mbox
from register import *
import mysql.connector
class MyStudent:
    def frams(self,root1):
        root1.title("STUDENT")
        root1.geometry("880x500")
        l=Label(root1,text="STUDENT DETAILS" )
        l.place(x=400 , y=50)
        username=Label(root1,text="USERNAME")
        entry1=Entry(root1)
        a=entry1.get()
        print(a)
        password=Label(root1,text="PASSWORD")
        entry2=Entry(root1)
        username.place(x=200,y=100)
        entry1.place(x=400,y=100)
        password.place(x=200 , y=200)
        entry2.place(x=400,y=200)
        def mybutton():
            conn = mysql.connector.connect(host='localhost', database='mocktest', user='root', password='shakshi')
            sql_select_Query = "select * from login"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            count=0
            for row in records:
                if entry1.get()==row[0]:
                    count=1
                    break
            cou=0
            for row in records:
                if entry2.get() == row[1]:
                    cou = 2
                    break
            if (count==1 and cou==2):
                mbox.showinfo("INFO","LOGIN SUCCESSFUL")
            else:
                root1.withdraw()
                mbox.showinfo("INFO","LOGIN UNSUCCESSFUL")
            cursor.close()
            conn.close()
        b1 = Button(root1, text="LOGIN", font="cyan",command=mybutton)
        b1.place(x=350, y=300)
        mr=MyRegister()
        def call():
            root3=Tk()
            mr.register(root3)
            root1.destroy()
            root3.mainloop()
        b2=Button(root1,text="New User?? Register Here",font="cyan",command=call)
        b2.place(x=300,y=350)


