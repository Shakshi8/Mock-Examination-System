from tkinter import *

class MyQuestion:
    def question(self):
        root4=Tk()
        root4.title("QUESTION")
        l=Label(root4,text="QUESTIONS")
        l.place(x=650,y=5)
        root4.geometry("1500x1500")
        s1=Button(root4,text="ADD")
        s1.place(x=500, y=50, width=50, height=20)
        s2= Button(root4,text="DELETE")
        s2.place(x=600, y=50, width=50, height=20)
        s3= Button(root4,text="DONE")
        s3.place(x=700,y=50,width=50,height=20)
        root4.mainloop()