from  tkinter import  *

root= Tk()

v= IntVar()

v.set(1)

languages=[
    ("Python",1),
    ("Android",2),
    ("HTML",3),
    ("Laravel",4),
    ("IOS",5),
           ]

def showChoice():
    print(v.get())

label = Label(root, text="Select A Course",padx=20, justify=LEFT).pack()

for val, language in enumerate(languages):
    Radiobutton(root, text=language, padx=20, variable=v, value=val,command=showChoice).pack(anchor=W)


root.mainloop()