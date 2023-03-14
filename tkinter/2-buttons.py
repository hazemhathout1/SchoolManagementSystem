from tkinter import*

root=Tk()


def myclick():
    mylabel=Label(root,text="I just clicked The button",fg="Blue",bg="#ffff01")
    mylabel.grid(row=0,column=1)

mybutton1=Button(root,text="Press here!",command=myclick,fg="Green",bg="Black")
mybutton2=Button(root,text="Press here!",state=DISABLED)
mybutton1.grid(row=0,column=0)
mybutton2.grid(row=1,column=0)



root.mainloop()