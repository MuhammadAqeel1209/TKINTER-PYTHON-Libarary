from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("List Box Tutorial")

def Add():
    global i
    listItem = ["Bread","Pizza","Burger","Sandwich","IceCream"]
    lbx.insert(ACTIVE,listItem[i])
    i += 1

i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First Item Of List Box")

Button(text="Add Item",command=Add).pack()


root.mainloop()