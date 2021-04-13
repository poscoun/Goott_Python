# 1.
for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j <= i:                # 세로 방향 변수 i만큼
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

# 2.
#입력 : int 자료형 1개(n)
#출력 : n 의 길이를 가지는 숫자 피라미드
n = 6

for i in range(n):       # 0부터 n-1까지 반복
    line_str = ''            #해당 줄의 문자열을 선언
    for j in range(i+1):         #0부터 i까지 반복
        line_str += str(j+1)         #해당 줄 문자열에 해당 숫자를 더한다.
    print(line_str)                     #해당 줄 출력

# 3.
n = int(input("몇줄 출력? "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

# 4.
for i in range(6):
    for j in range(6):
        if j >= i:
            print('*', end='')
    print()

# 5.

n = int(input("입력 : "))

if n % 3 == 0:
    print("{}는 3의 배수입니다.".format(n))
elif n % 3 != 0:
    print("{}는 3의 배수가 아닙니다.".format(n))

# 6.

for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n == 4:
            print(n1, n2)