A=int(input("1.입력한 수식 계산 2. 두 수 사이의 합계: "))

if A==1:
    B=input(" ***수식을 입력하세요: ")
    answer=eval(B)
    print(B,"결과는",answer,"입니다.")

elif A==2:
    C=int(input(" ***첫 번째 숫자를 입력하세요: "))
    D=int(input(" ***두 번째 숫자를 입력하세요: "))
    answer=(C+D)/2*(D-C+1)
    print(C,"+...+",D,"는",answer,"입니다.")
else
print("1 또는 2만 입력해야 합니다.")
