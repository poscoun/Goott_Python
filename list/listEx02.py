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

# 리스트에 요소 삽입 : insert
# insert(x, y) : x번째 위치에 y 값을 삽입
c.insert(3, 4)
print(c)

# 리스트 요소 제거 : remove
c.remove(4)
print(c)

c.insert(3, 40)
print(c)

c.remove(40)    # 중복되는 값이 있으면 첫번째 요소만 삭제
print(c)

# 리스트 요소 꺼내기 - pop
d = [1, 2, 3]
d.pop()
print(d)

# pop(x) : x번째 요소를 삭제
e = [1, 2, 3, 4, 5]
e.pop(3)
print(e)

# 리스트에 포함된 요소의 갯수 세기 : count
f = [10, 20, 20, 30, 30, 30]
print(f.count(30))

# 리스트 확장 : extend
g = [1, 2, 3]
g.extend([4, 5])
print(g)
g.extend([6, 7])
print(g)

g += [8, 9]
print(g)

