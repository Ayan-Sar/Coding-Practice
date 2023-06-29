from tkinter import *
root = Tk()
root.geometry("1500x1300")
def myclick():
    mylabel=Label(root, text= "Haat sala...number kon dega tereko???Tujhe toh Elon Musk ka pochamarne wala ke bhi number nhi denge...")
    mylabel.pack()
mybtn=Button(root, text="Click me to get the phone number of Elon Musk" , fg="White" , bg="Brown", padx=50, pady = 30, command=myclick)
mybtn.pack()
root.mainloop()