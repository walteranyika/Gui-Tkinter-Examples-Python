import  tkinter as tk

root = tk.Tk()
v= tk.IntVar()

label = tk.Label(root, text="Choose Your course").pack()

tk.Radiobutton(root,
               text="Python",
               padx=20,
               variable=v,
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="Android",
               padx=20,
               variable=v,
               value=2).pack(anchor=tk.W)

root.mainloop()