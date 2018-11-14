import  tkinter as tk
# https://www.python-course.eu/tkinter_radiobuttons.php
counter = 0
def clicked(label):
    global  counter
    counter+=1
    # label.config(text=str(counter))
    # label.config(text=str(counter))
    print("Button hass been clicked "+str(counter))
root = tk.Tk()

button = tk.Button(root, text="Click Me", fg="red", command=quit).pack(side=tk.BOTTOM)

label = tk.Label(root,  fg="green").pack()

button2= tk.Button(root, text="Increase", fg="red", command=clicked(label)).pack(side=tk.TOP)

root.mainloop()



