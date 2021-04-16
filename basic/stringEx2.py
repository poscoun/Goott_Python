str = '오직 한 가지 성공이 있을 뿐이다. 바로 자기 자신만의 방식으로 삶을 살아갈 수 있느냐이다.'

print(str)

print(str[3])
# 문자열 인덱싱(색인 연산) : 문자를 배열에 담아서 번호를 부여한 것
# 인덱스는 0 부터 시작함에 유의
# 파이썬의 특별한 기능 : 문자를 뒤에서부터 읽어올 수 있음
print(str[-2])
# -0과 0은 같으므로 -1부터 시작
print('-----------------------------------------')
print(str[8:11])    # 문자열 슬라이싱 기법
# 처음자리수 <= 변수 < 끝자리수

print(str[0:3]) # 공백도 출력되고 있음에 유의
# '모든' 과 ' 모든 ' 은 엄염히 다른 문자이니 유의!

#  끝번호를 생략하면 그 문자열의 끝까지 돌려줌
print(str[10:])

# 반대로 시작번호를 생략하면 문자열의 처음부터 지정한 끝번호자리까지 return
print(str[:11])

# 시작번호, 끝번호 모두를 생략
print(str[:])

# 인덱싱과 마찬가지로 - 기호 사용 가능
print(str[11 : -7])

# 실습
hiredate = '20210412MON'

# year, date, day로 구분하여 출력하세요
year = hiredate[0:4]
date = hiredate[4:-3]
day = hiredate[8:]
print(year, date, day)

