inFp=None
inList,inStr=[],""
num=1

inFp=open("C:/Users/LGPC/Desktop/Homework/txt/data1.txt","r",encoding="utf-8")

inList=inFp.readlines()
for inStr in inList:
    print(num,":",inStr,end="")
    num+=1

inFp.close()