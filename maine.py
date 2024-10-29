from tkinter import* 




window = Tk()
window.title("Event handeler")
window.geometry("100x100")




def handle_keepress(event) :
 if (event.char == "w"):
   print("charecter is moving up")

 elif (event.char == "s" ):
   print("charecter moving down")

 elif (event.char == "a" ):
   print("charecter moving left")

 elif (event.char == "d" ):
   print("charecter moving right")
   

window.bind("<Key>" , handle_keepress)

window.mainloop()