class Human():
    pass

person = Human()
person.name = '홍길동'
person.height = '188.6'

print(person.name)

print('---------------------------------')
def create_human(name, height):
    person = Human()
    person.name = name
    person.height = height
    return person

Human.create = create_human

person = Human.create('홍길동', 188.6)
print(person)
print(person.name)

print('----------------------------------')
'''
# 이 홍길동이 먹고, 걷도록 하고 싶어요
# 함수 : eat(), walk()
# 출력 : eat - 홍길동이 건강하게 먹어서 188.7이 되었어요
        walk - 홍길동이 운동을 해서 188.8이 되었어요
'''
# 먹기
def eat(person):
    person.height += float(0.1)
    print('{} 이 건강하게 먹어서 {}이 되었어요'.format(person.name, person.height))

# 걷기
def walk(person):
    person.height += float(0.2)     # 실수 계산은 정밀성을 가지지는 않음
    print('{}이 운동을 해서 {} 가 되었어요'.format(person.name, person.height))

# Human 클래스 내부 함수로 인식
Human.eat = eat
Human.walk = walk

# 실체화 -> 모델링
person.eat()
person.walk()
