from tkinter import *
from admin import *
from student1 import *
root=Tk()
root.title("MOCK TEST")
root.geometry("500x500")
my=MyStudent()
ms=MyAdmin()
def admin():
    root2=Tk()
    root.destroy()
    ms.frama(root2)
    root2.mainloop()
def student():
    root1=Tk()
    root.destroy()
    my.frams(root1)
    root1.mainloop()
b1=Button(root,text="ADMIN",font="cyan",command=admin)
b2=Button(root,text="STUDENT",font="cyan",command=student)
b1.place(x=100,y=100,width=100,height=100)
b2.place(x=300,y=100,width=100,height=100)
root.mainloop()

