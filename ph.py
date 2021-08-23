from tkinter import *
root=Tk()
root.title("GREET USER")
root.geometry("300x300")

def click():
    name=entry.get()
    show=str("Hello Dear "+ name +"!")
    mesg['text']=show
label=Label(root,text="Enter your name :",font=("times",16))
label.place(x=20,y=20)

entry=Entry(root,text="")
entry.place(x=175,y=25,width=100,height=20)
Button(root,text='click Me',command=click,fg='green',font=('times',16)).place(x=100,y=200)
mesg=Label(text="",font=("times",16),fg='blue')
mesg.place(x=50,y=100)
mainloop()