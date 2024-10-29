from tkinter import* 
from tkinter import messagebox


window = Tk()
window.title("Event handeler")
window.geometry("100x100")

def msg():
    messagebox.showerror("Alert","Stop! virus found" )


btn = Button(window,text="Scan for virus",command = msg)
btn.place(x = 640, y = 380)


window.mainloop()