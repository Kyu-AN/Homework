from tkinter import *

window=Tk()

photo1 = PhotoImage(file="gif/Homer.gif")
label1=Label(window,image=photo1)
label1.pack(side="left")

photo2 = PhotoImage(file="gif/Homer2.gif")
label2=Label(window,image=photo2)
label2.pack(side="left")

window.mainloop()