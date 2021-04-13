print()
'''
# 리스트 관련 함수들
'''

# 리스트에 요소 추가 : append
a = [10, 20, 30]
a.append(40)
print(a)

a = [10, 20, 30]
a.append([50, 60])
a.append('hihi')
print(a)

# 리스트 정렬 : sort
b = [9, 4, 2, 10, 7]
b.sort()
print(b)

# 문자는 알파벳 순서로 정렬
str = ['wow', 'fantastic', 'python']
str.sort()
print(str)

# 리스트 역순 : reverse
# 알파벳 역순(내림차순)이 아니고 그대로 역순서임에 유의!
str = ['world', 'hello', 'python']
str.reverse()
print(str)

# 위치 반환 : index - 리스트에 찾는 값이 있으면 위치값을 리턴
c = [10, 20, 30, 40, 50]
print(c.index(40))  # 위치값이 인덱스 번호임에 유의
# print(c.index(60))  # 찾는 값이 없으면 error

