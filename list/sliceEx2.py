print()

list1 = list(range(20))

print(list1)

# 5부터 15까지 출력
print(list1[5:16])

# 값을 건너뛰면서 가져오려면? step
# 시작:끝:step
print(list1[5:16:2])
print(list1[5:18:3])

# list1이 5, 8, 11, 14 값을 가지도록 슬라이스
print(list1[5:15:3])
# list1이 5, 9, 13, 17 값을 가지도록 슬라이스
print(list1[5:18:4])

print('-------------------------------------')
list2 = list(range(10))
print(list2)

# 특정 영역값을 바꾸기
print(list2[1:3])

list2[1:3] = [55, 66]
print(list2)

# 기존 값의 개수와 바꾸려는 값의 개수가 똑같아야 하는 것은 아님
list2[1:3] = [77, 88, 99]
print(list2)

list2[1:3] = [5]
# 바꾸는 수는 반드시 리스트형으로 써야 함에 유의
# list2[1:3] = 5 - error
print(list2)

print('------------------------------------------')
list3 = list(range(5))
print(list3)

# 최종 출력 : [0, 11, 22, 33, 4]
list3[1:4] = [11, 22, 33]
print(list3)
