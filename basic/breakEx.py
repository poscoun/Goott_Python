print()
# 1부터 사용자가 입력한 숫자까지만 출력 (단, 1000 이하)

'''
value = input('숫자 입력하세요 (단, 1000 이하) : ')

num = int(value)

for i in range(1, num+1):
    if i >= num+1 :
        break
    print(i)
'''

print('----------------------------------------')
# break : break 붙어 있는 가장 가까운 반복문을 탈출
# continue : 이번만 생략 나머지는 수행
for i in range(1,5) :
    for j in range(1, 5):
        if(i==j) :
            #break
            continue
        print(i, ' : ', j)