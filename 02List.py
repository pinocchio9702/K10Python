'''
파일명 : 02List.py

파이썬에는 연속된 collection데이터 구조에
list, tuple, dictionary, set이 있다.

리스트(list) 
    : 대괄호[] 안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할 수 있는
    시퀀스 자료형(Mutable 데이터 타입) 서로 다른 자료형의 항목으로 구성할 수 있음
    인덱싱, 슬라이싱, 연결, 반복 등 가능함
'''
#기본적인 선언과 사용법은 배열과 동일함
list1 = [1,2,3,4,5]
list2 = ['Java', 'HTML', 'Python']
list3 = [10, 20, ['Java', 'HTML', 'Python']]
print('list1:', list1) #배열 전체가 출력됨
print('list2[2]:', list2[2])
print('lis3t[2]', list3[2]) #리스트내의 리스트가 출력됨

#슬라이싱
print('list1[1:4]', list1[1:4])
print('list1[:3]', list1[:3])
print('list1[1:]', list1[1:])

all_list = [list1, list2]
print('all_list : ', all_list)
print('all_list[1][0]', all_list[1][0])

#list 관련 메소드
list1.append(6)
print('append(6)=>', list1)

list1.clear()
print('clear()=>', list1)

list1.extend([10, 20, 30, 40, 50])
print('extend=>', list1)
list1.insert(1, 99)
print('insert=>', list1)

print(list1.pop()) #리스트의 마지막 항목 반환 및 삭제
print('pop()=>', list1)

list1.remove(99) #처음 나오는 항목 99 삭제
print('pop()=>', list1)

list1.reverse
print('reverse() => ', list1)

'''
List Comprehension
    : 대괄호 안에 for루프로 반복적인 표현식을 실행해서
    리스트 요소들을 초기화 하는 방법
    형식]
        [표현식 for 요소 in 컬렉션 [if조건식]]
'''

#0~9까지의 정수중 3의 배수의 제곱으로 이루어진 리스트 초기화
list = [n ** 2 for n in range(10) if n%3==0]
print(list)