# 반복문
# for 반복문
# for 변수 in fange() :
#       수행해야할 문장1
#       수행해야할 문장2
#           .
#           .

# range() : 숫자 리스트를 자동으로 만들어 주는 함수
list = range(10)
print(list) # 0부터 10미만의 정수를 자동으로 생성

# 시작, 끝 숫자를 지정하려면 콤마(,)로 구분
list = range(1,11)
print(list)


# 끝 숫자가 미만임에 유의
for i in range(1,11):
    print('for 반복문',i)

print('--------------------------------------------')
for i in range(1,10):
    print(i,' 번쨰','3*',i,'=',(3*i))

print('--------------------------------------------')
# 사용자로부터 하나 입력 구구단 출력 5단

value = input('숫자입력해 : ')
dan = int(value)

for i in range(1,10):
    print((i*dan))