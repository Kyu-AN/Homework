inFp=None
inStr=""
num=1

inFp=open("C:/Users/LGPC/Desktop/Homework/txt/data1.txt","r",encoding="utf-8")

while True:
    inStr=inFp.readline()
    if inStr=="":
        break;
    print(num,":",inStr,end="")
    num+=1

inFp.close()