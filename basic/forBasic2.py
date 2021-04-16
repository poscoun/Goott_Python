# 다중반복문
# 19단 출력

for dan in range(2,20) :
    for j in range(1,20) :
        print(dan,"X",j,'=',(dan*j))
    print()

print('-------------------------------')
# 1~ 16까지 짝수 출력
for i in range(1,17):
    if i%2==0:
        print(i)


print('-------------------------------')
# 1~10 출력 - 옆으로 출력
for i in range(1,11):
    print(i, end="")

print()
print('-------------------------------')

# 1~10합
sum = 0
for i in range(1,11):
    sum +=i
print(sum)


