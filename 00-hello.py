
# 기본 연습 1 : 숫자

a = 2
b = 3

print(a+b)

c = a+b

print(c)


# 기본 연습 2 : 문자열

a = 'ye-seung'
b = ' kim'

print(a+b)


# 리스트 배열 출력

a_list = ['사과', '배', '감']

print(a_list[0])

# 리스트 배열에 추가하기

a_list.append('수박')

print(a_list)


# 딕셔너리 자료형 입력 및 출력 연습

a_dict = {
    'name' : 'bob',
    'age' : 27
}

print(a_dict['name'])


# def 함수 예제 1

def sum(a,b) : 
    print('더하자!')
    return a+b

result = sum(1,2)
print(result)


# def 함수 예제 2

def is_adult(age) :
    if age > 20 :
        print('성인입니다')
    else : 
        print('청소년입니다')
        
is_adult(15)


# 리스트 출력 연습

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

for fruit in fruits :
    print(fruit)

for aaa in fruits :
    print(aaa)
    

# 조건문 연습 1

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for aaa in fruits :
    if aaa == '사과' :
        count += 1

print(count)


# 조건문 연습 2

people = [{'name': 'bob', 'age': 20}, 
            {'name': 'carry', 'age': 38},
            {'name': 'john', 'age': 7},
            {'name': 'smith', 'age': 17},
            {'name': 'ben', 'age': 27}]

for person in people :
    print(person)
    
for ppp in people :
    if ppp['age'] > 20 :
        print(ppp['name'])
        

