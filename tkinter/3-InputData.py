from tkinter import*

root=Tk()

e=Entry(root,width=30,borderwidth=5) 
e.grid(row=0,column=0)

def myclick():
    mylabel=Label(root,text="Hello "+e.get())
    mylabel.grid(row=2,column=0)

mybutton1=Button(root,text="Enter Your Name",command=myclick,fg="Red",bg="White")
mybutton1.grid(row=1,column=0)







root.mainloop()