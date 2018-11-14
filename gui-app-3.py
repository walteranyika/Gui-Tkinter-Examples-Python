import  tkinter as tk

counter = 0

def  counter_label(label):
    def count():
         global  counter
         counter+=1
         label.config(text=str(counter))
         label.after(1000,count)
    count()

root = tk.Tk()

root.title("Counting The Clicks")

label = tk.Label(root, fg="green")
label.pack()
counter_label(label)

btn = tk.Button(root, text='STOP', width=25, command= root.destroy).pack()

root.mainloop()

