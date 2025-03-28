select=int(input("입력 진수 결정(16/10/8/2): "))
A=input("값 입력: ")

if select != 16 and select != 10 and select != 8 and select != 2:
    print("16,10,8,2 중에서 선택해주세요")
else:
    if select == 16:
        B=int(A,16)
    if select == 10:
        B=int(A,10)
    if select == 8:
        B=int(A,8)
    if select == 2:
        B=int(A,2)

    print("16진수 ==> ",hex(B))
    print("10진수 ==> ",B)   
    print("8진수 ==> ",oct(B))   
    print("2진수 ==> ",bin(B)) 