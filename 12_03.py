import threading

class Number:
    def __init__(self,n):
        self.n=n

    def cal(self):
        total=sum(range(1,self.n+1))
        print("1+2+3+.....+%d = %d"%(self.n,total))

n1=Number(1000)
n2=Number(100000)
n3=Number(10000000)

th1=threading.Thread(target=n1.cal)
th2=threading.Thread(target=n2.cal)
th3=threading.Thread(target=n3.cal)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()