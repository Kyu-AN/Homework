from tkinter import *
from time import *

frameList=["B&M.gif","Bart.gif","Family.gif","Homer.gif","Homer2.gif","Lisa.gif","Maggie.gif","Marge.gif","Ralph.gif"]

photoList=[None]*9
num=0

def clickNext():
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file="gif/"+frameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    nameLabel.config(text=frameList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="gif/"+frameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    nameLabel.config(text=frameList[num])

window=Tk()
window.geometry("500x500")
window.title("사진 앨범 보기")

btnPrev=Button(window,text="<< 이전",command=clickPrev)
btnNext=Button(window,text=">> 다음",command=clickNext)

photo=PhotoImage(file="gif/"+frameList[0])
pLabel=Label(window,image=photo)
nameLabel = Label(window, text=frameList[0], font=("Arial", 12))

btnPrev.place(x=100, y=10)
nameLabel.place(x=210, y=15)
btnNext.place(x=330, y=10)
pLabel.place(x=10,y=50)

window.mainloop()