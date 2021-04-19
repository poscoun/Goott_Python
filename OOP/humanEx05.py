print()
'''
# 특수한 메소드 : 메소드 이름 양쪽에 __ 두개
# 구글 검색 : python specil attributes
'''
class Human():
    # 초기화 메소드
    def __init__(self):
        pass
        print('__init 실행')

    def __init__(self, name, height):
        print('__init__ 실행')
        print('이름 : {}, 키 : {}'.format(name, height))

    def __init__(self, name, height):
        self.name = name
        self.height = height

    # 문자열화 메소드 : 인스턴스를 문자열로 변환할 때 어떻게 표현할지를 결정
    def __str__(self):
        return "이름 : {}, 키 : {} ".format(self.name, self.height)

# person = Human()

# person = Human('홍길동', 178.8)
# print(person.name)

person = Human('유관순', 160.3)
print(person)

