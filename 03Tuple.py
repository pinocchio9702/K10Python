'''
파일명 : 03Tuple.py

튜플(Tuple)
    : 소괄호() 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형.
    서로다른 자료형으로 구성할 수 있지만, 대입연산자로 튜플의 항목을
    변경할 수 없는 Immutable 테이터 타입
'''

tu1 = tuple() #빈 튜플 생성
tu2 = (1,2,3,4,5)
#1개의 항목을 갖는 튜플생성 뒤에 컴마가 없으면 단순한 변수생성.
tu3 = 1,
tu4 = (98,99,100)
print(tu1, tu2, tu3)

print("tu2[0]:", tu2[0])
print("tu2[-1]:", tu2[-1])#마지막 항목을 출력함.
print("tu2[1:3]:", tu2[1:3])

#해당 요소가 포함되었는지 확인
print("4 in tu2:", 4 in tu2)
print("99 not in tu2", 99 not in tu2)
print("tu2 * 3:", tu2 * 3)

new_tu = tu2 + tu4
print("new_tu", new_tu)

my_list = [1,2,3]
my_tuple = ('x', 'y', 'z')
print(tuple(my_list))
print(tuple(my_tuple))