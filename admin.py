from tkinter import *
from question import *
import mysql.connector
from tkinter import messagebox as mbox
class MyAdmin:
    def frama(self,root2):
        root2.title("ADMIN")
        root2.geometry("880x500")
        l=Label(root2,text="Admin Login" )
        l.place(x=400 , y=50)
        username=Label(root2,text="USERNAME")
        entry1=Entry(root2)
        password=Label(root2,text="PASSWORD")
        entry2=Entry(root2)
        username.place(x=200,y=100)
        entry1.place(x=400,y=100)
        password.place(x=200 , y=200)
        entry2.place(x=400,y=200)
        mq = MyQuestion
        def mybutton():
            conn = mysql.connector.connect(host='localhost', database='mocktest', user='root', password='shakshi')
            sql_select_Query = "select * from login"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            count = 0
            for row in records:
                if entry1.get() == row[0]:
                    count = 1
                    break
            cou = 0
            for row in records:
                if entry2.get() == row[1]:
                    cou = 2
                    break
            if (count == 1 and cou == 2):
                mq.question(self)
            else:
                mbox.showinfo("INFO", "LOGIN UNSUCCESSFUL")
            cursor.close()
            conn.close()
        b = Button(root2, text="LOGIN", font="cyan",command=mybutton)
        b.place(x=350, y=300)




