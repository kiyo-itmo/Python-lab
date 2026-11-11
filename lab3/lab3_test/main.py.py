import tkinter as tk

root =tk.Tk()
root.title("My App")
root.geometry("500x400")


image = tk.PhotoImage(file="bg_pic.png")

label = tk.Label(root, image= image)
label.place(x=0, y=0)



root.mainloop()