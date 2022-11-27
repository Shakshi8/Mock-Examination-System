from tkinter import *
import mysql.connector

class MyRegister:
    def register(self,root3):
        root3.title("REGISTRATION")
        root3.geometry("1000x1000")
        l = Label(root3, text="REGISTRATION PROCEDURE")
        l.place(x=300, y=50)
        username = Label(root3, text="USERNAME")
        entry1 = Entry(root3)
        name = Label(root3, text="NAME")
        entry2 = Entry(root3)
        rollno = Label(root3, text="ROLLNO")
        entry3 = Entry(root3)
        dob = Label(root3, text="DATE OF BIRTH")
        entry4 = Entry(root3)
        password=Label(root3,text="PASSWORD")
        entry5=Entry(root3)
        username.place(x=300, y=100)
        entry1.place(x=400, y=100)
        name.place(x=300, y=200)
        entry2.place(x=400, y=200)
        rollno.place(x=300, y=300)
        entry3.place(x=400, y=300)
        dob.place(x=300, y=400)
        entry4.place(x=400, y=400)
        password.place(x=300, y=500)
        entry5.place(x=400, y=500)
        def mybutton():
            conn = mysql.connector.connect(host='localhost', database='mocktest', user='root', password='shakshi')
            cursor = conn.cursor()
            str="insert into login(username,password,name,rollno,dob)values (entry1,entry5,entry2,entry3,entry4)"
            try:
                cursor.execute(str)
                conn.commit()
                print('1 row inserted...')
            except:
                conn.rollback()
            cursor.close()
            conn.close()
        b = Button(root3, text="REGISTER", font="cyan",command=mybutton)
        b.place(x=350, y=600)
