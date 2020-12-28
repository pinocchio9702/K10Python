#파일명 : 11builtinFunction.py
'''
Built-in Function(내장함수)
    : 내장함수는 외부모듈과 달리 import가 필요하지 않기 때문에
    아무런 설정없이 바로 사용할 수 있다.
    int(), print(), max(), input()과 같은 함수가 있다.
'''
print('=' *30)
print('enumerate()')
'''
enumerate()
    : 순서가 잇는 자료형(리스트, 튜플, 문자열)을 입력받아
    인덱스 값을 포함하는 enumerate객체를 반환한다.
'''
print('='*30)
data =['Naver', 'Kakao','Google']
for i, v in enumerate(data):
    print(i, v)

'''
eval()
    : 실행가능한 문자열을 입력받아 실행한 결과값을 반한다.
'''
print('='*30)
print('eval()')
print('='*30)
print(eval('1+2'))
print(eval("'hi'+ 'a'"))

'''
sorted()
    : 입력값을 정렬한 후 리스트로 반환한다.
'''
print('='*30)
print('sorted()')
print('='*30)
numbers= (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
print(sorted(numbers))

'''
제너레이터 
    : 연속적인 값을 차례로 생성할 수 있다.
    데이터를 미리 만들어 놓지 않아도 되므로 메모리를 절약할 수 있다.
    return문 대신 yield문을 사용하여 반복 가능한 객체를 생성한다.
'''
print('='*30)
print('제너레이터')
print('='*30)

print('yield의 동작 과정')
def number_generator1():
    yield 0 # 0을 함수 바깥으로 전달하면서 코드 실행을 함수밖으로 양보한다.
    yield 1 # next()를 통해 순차적으로 yield가 실행된다.
    yield 2 
g = number_generator1()
print('next(g)', next(g))
print('next(g)', next(g))
print('next(g)', next(g))

'''
for문을 반복할때마다 next()를 자동으로 호출하므로
yield에서 발생시킨 값을 순차적으로 가져올 수 있다.
'''
def number_generator2(n):
    i = 0
    while i<n:
        yield i # yield가 실행될때 현재 i값이 for문으로 전달되어 출력됨
        i += 1
for i in number_generator2(5): #for문에서 호출될때 자동으로 next()가 실행됨
    print(i)
#실행결과 : 0 1 2 3 4
def upper_generator(val):
    for i in val:
        yield i.upper() # 문자열을 대문자로 변경한 후 함수밖으로 전달함
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits): # 리스트의 인자만큼 반복 호출됨
    print(i, end=' ')
# 실행결과 : 리스트의 문자열이 대문자로 출력됨