from  tkinter import *
from  tkinter.ttk import  *
from  tkinter import  messagebox

# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
def show_details():
    print("Choosen Value is "+combo.get())
    # messagebox.showinfo("Title",'Geeky Forever')
    res=messagebox.askyesno('Quit','Do yo want to cance?')
    print(res)


root= Tk()

root.title("Como Box")

root.geometry('300x200')

combo =Combobox(root)

combo["values"]=("Kenya","Uganda","Tanzania","Rwanda","Burundi","Ethiopia","Egypt")

combo.current(1)

combo.grid(row=0)

Button(root,text="Show Choosen",command=show_details).grid(row=1, column=0)



mainloop()