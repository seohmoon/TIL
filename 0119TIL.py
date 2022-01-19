# 0119 TIL
# 숫자를 받아서 (input)
# 세제곱 결과를 반환 (output)
# 호출 : cube(2), cube(10), cube(100)
def cube(number):
    return number * number * number
    # return number ** 3 으로 써줘도 됨

print(cube(2))
print(cube(10))
print(cube(100))

# 직사각형 넓이와 둘레
def rectangle(width, height):
    return width * height, (width + height) * 2

print(rectangle(30, 20))
# => (600, 100) 하나의 튜플이다!! 

#add
def add(x, y):
    return x + y

print(add(1, 2)) # 위치 - 내부에서 바인딩 x = 1, y = 2
print(add(y = 2, x = 1)) # 키워드 - 내가 직접 x와 y 값을 각각 지정
#print(add(x = 1, 2)) # => SyntaxError: positional argument follows keyword argument
#신택스 에러 발생(문법적 에러) point는 follows
# ㄴ 키워드로 지정하는 순간 위치는 이미 의미가 없어짐 => 에러
print(add(1, y=2)) #얘는 작동함 위치지정 키워드! 
#prin(add(1, 2, 3)) 하면 2개 받는건데 3개라 오류뜸


#input 2 *별이 한개
print('hi', 'hello', '안녕', 'Guten Morgen', 'Bon jour')

def add(*args):
    print(args, type(args))

add(1, 2, 3) # => 리턴값은 넌
add(1) # => 리턴값은 넌


#family **별이 두개
def family(**kwagrs):
    print(kwagrs, type(kwagrs))

family(father='고길동', monster='둘리')



### local_global
def ham():
    a = 'spam'

#1.
#print(a) #NameError: name 'a' is not defined

#2.
#ham()
#print(a) #NameError: name 'a' is not defined

#함수는 가장 기본 : local scope!
#블랙박스의 결과를 받아보고 싶으면 반환 값을 변수에 저장해서 사용하는 것!
#블랙박스 밖으로 결과를 주고 싶을 수 있어요! => return 해야해요!!

PI = 3.141592
first_name = 'tak'
student = '종은'
students = ['', '']

def get_first_name():
    pass

def foo(*args):
    pass



#람다함수
def odd(n):
    return n % 2

print(list(filter(odd, range(5))))
print(list(filter(lambda n: n % 2, range(5))))


# module 
import random

print(random.sample(range(1, 46), 6))

#복잡한 딕셔너리
#import pprint # 예쁘게 출력해줌 사용할 땐 pprint.pprint(a)
from pprint import pprint #위랑 같음, 사용할 땐 pprint(a)
a = {'a': ['apple', 'ant'], 'b': 'banana', 'c ':'car', 'd': 'drive', 'e': ['error', 'eat']}
print(a)
pprint(a)



#Python에서 기본으로 사용할 수 있는 built-in 함수 찾아 볼 때
#print(dir(__builtins__))

a = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

print(*a)

a=[{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
tem=[]
j = 0
    for k in a:
        tem[j]=k
        j = j + 1
print(tem)

def dict_list_sum(a):
    tem :[]
    j = 0
    for k in a:
        tem[j] = k
        j = j + 1
    a.values()
    age_sum = 0
    for i in dict_values:
        age_sum = age_sum + i
    return age_sum

print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))


def dict_list_sum(a):
    a.values()
    age_sum = 0
    for i in dict_values:
        age_sum = age_sum + i
    return age_sum

print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))

##########
a=[{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum_age = 0
for b in a:
    b = b['age']
    sum_age = sum_age + b
print(sum_age)