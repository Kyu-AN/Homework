from tkinter import *
from tkinter import messagebox

def shift_left(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + ←")

def shift_up(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + ↑")

def shift_right(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + →")

def shift_down(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + ↓")

window=Tk()

window.bind("<Shift-Left>", shift_left)
window.bind("<Shift-Up>", shift_up)
window.bind("<Shift-Right>", shift_right)
window.bind("<Shift-Down>", shift_down)

window.mainloop()