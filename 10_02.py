from tkinter import *
import random

btnlist=[None]*9
frameList=["B&M.gif","Bart.gif","Family.gif","Homer.gif","Homer2.gif","Lisa.gif","Maggie.gif","Marge.gif","Ralph.gif"]

random.shuffle(frameList) 


photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("840x840")

for i in range(0,9):
    photoList[i]=PhotoImage(file="gif/"+frameList[i])
    btnlist[i]=Button(window,image=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnlist[num].place(x=xPos,y=yPos)
        num += 1
        xPos += 280
    xPos = 0
    yPos += 280

window.mainloop()