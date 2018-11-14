from  tkinter import  *




root = Tk()

root.title("Inputs and Clicks")

root.geometry('350x200')

labelA = Label(root, text="First Name").grid(row=0)
labelB = Label(root, text="Last Name").grid(row=1)


inputA= Entry(root)
inputA.focus()
inputA.grid(row=0, column=1)
inputB= Entry(root)
inputB.grid(row=1, column=1)

labelC= Label(root,text="Result Here")
labelC.grid(row=3)
def show_entries():
    labelC.config(text="First Name: %s\nLast Name: %s" % (inputA.get(), inputB.get()))
    print("First Name: %s\nLast Name: %s" % (inputA.get(), inputB.get()))

Button(root, text='Quit', command=quit).grid(row=2, column=0, sticky=W, pady=4)
Button(root, text='Show', command=show_entries).grid(row=2, column=1, sticky=W, pady=4)

mainloop()