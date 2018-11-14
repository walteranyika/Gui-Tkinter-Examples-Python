import tkinter as tk
print(tk.TkVersion)

root = tk.Tk()

# logo=  tk.PhotoImage(file="user.gif")
#
# w1= tk.Label(root, image=logo).pack(side="right")

text= """parameter can be used to justify a text on the LEFT, RIGHT or CENTER. padx can be used to
         add additional horizontal padding around a text label. The default padding is 1 pixel. pady
         is similar for vertical padding. The previous example without justify (default is centre)
         and padx looks like this"""

w2= tk.Label(root,
             justify=tk.CENTER,
             padx=10,
             text=text).pack(side="left")

tk.Label(root,
         text="This is red text",
         fg="blue",
         bg="white",
         font="Verdana 10 bold" ).pack()

root.mainloop()