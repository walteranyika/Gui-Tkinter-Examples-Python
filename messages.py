import tkinter as tk

master = tk.Tk()

text = "Whatever you do will be insignificant but its very important that you do it"

message = tk.Message(master, text=text)

message.config(fg="blue",bg="white", font=('times', 24, 'italic'))

message.pack()

master.mainloop()