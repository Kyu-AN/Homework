import os

inFp,outFp=None,None
inStr=""
fName1=input("소스 파일명을 입력하세요 : ")
fName2=input("타깃 파일명을 입력하세요 : ")

if os.path.exists(fName1):
    inFp=open(fName1,"r",encoding="utf-8")
    inList=inFp.readlines()

    if os.path.exists(fName2):
        outFp=open(fName2,"w",encoding="utf-8")
        for inStr in inList:
            outFp.writelines(inStr)
        inFp.close()
        outFp.close()
        
    else:
        print("%s 파일이 없습니다."% fName2)
        inFp.close()

else:
    print("%s 파일이 없습니다."% fName1)