'''
반복문
    : 파이썬에서의 반복문은 while문과 for문만 있다.
    do~while문은 없다.
'''

str = 'python'
#str이 공백이 될때까지 반복한다. 공백이 아니면 true
while str: 
    #출력문 끝에 공백을 추가하여 줄바꿈없이 출력한다.
    print(str, end=' ')
    '''
    문자열에서 첫글자를 제거한 후 대입한다.
    인덱스 1부터 끝까지 슬라이싱 한다.
    '''
    str = str[1:]
print()
print("===============")

#시나리오] 1~10까지의 합을 구하시오
'''
    python에서는 while구문에 else를 추가할 수 있다.
    while문의 조건에 위배되어 탈출하면 else구문이 실행된다.
'''
sum = 0
i = 1
while i <=10:
    sum += i
    if i<10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    i += 1
else :
    #while문을 벗어나면 실행됨
    print(sum)

#시나리오] 구구단을 출력하되 짝수단만 출력하시오
dan = 2
while dan <=9:
    if dan%2 == 1: #단이 홀수이면 while문의 처음으로 돌아감.
        dan += 1
        continue
    else: #단이 짝수일때만 구구단 출력
        su = 1
        while su <=9:
            #print()문을 서식에 맞춰서 사용하는 형태
            print("%2d * %2d = %2d" % (dan, su, su*dan), end=' ')
            su += 1
    dan += 1
    print()
print()