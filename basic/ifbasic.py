# 조건문(분기문)
# if 조건 :
#   수행할 문장1
#   수행할 문장2
#   .
#   .


people = 1

if people:
    print('사람이 한 명 들어있어요')


# 들여쓰기 중요 : 코드 블록을 구분해 주는 역할
# 탭 또는 스페이스바 4칸을 이용하여 들여쓰기 수행하면됨(cf. pyt
# hon2.x 라면 호용안됨)ㅒ

if people:
    print('사람이 한명있습ㄴ다.')
    # print('사람이 두 명 들어있을지도 몰라여')

# 참.거짓을 구분하는 논ㄴ리연산자(비교,논리적) 사요
x=3
y=2
if x !=y:
    print('x와 y는 갑지 않다')

    print(';----------------------------------------')

# 블록 - 클록(;) 다음에 들여쓴 코드 블록
#     - 같은 실행 흐름에서 순서대로 실행되는 코드 덩어리
#     - 여러 줄로 작성이 가능. 단, 여러 줄일 경우 들여쓰기 칸 수가 모두 같아야함


# 논리 연산자 : true, false
if True:
    print('블록 코드')
    print('같은 블록')
    print('여러줄 가능')

#블록을 끝내려면 들여쓰기를 끝내줘야 함 - 내어쓰기

# ㅁ한번이라도 내어 쓴 블록은 끝나 블록이 되고, 다시 열 수 없습니다.

if True:
    print('첫본째 블록 코드')
    # 블록 안에는 또 다른 블록이 들어갈 수 있으
    if False:
        print('실행되지 안흥ㄹ 코드')
    if True:
        print('첫번째 - 안쪽 블록 코드')

    print('첫번째 블록 끝ㅌ 코드')


print('----------------------------------------')

if True:
    print('첫본째 블록 코드')
    # 블록 안에는 또 다른 블록이 들어갈 수 있으
    if False:
        print('실행되지 안흥ㄹ 코드')
    if True:
        print('첫번째 - 안쪽 블록 코드')

    print('첫번째 블록 끝ㅌ 코드')
print('바깥 코드')


print('----------------------------------------')

# 분기
# if <조건> :
#    <코드블록>
#else :
#    <코드블록>

# 조건이 True이면 if 코드 블록을 싱행
# 조건이 False이면 else 코드 블록을 실행


print('----------------------------------------')
# 둘 중 큰 수 구 하기
num1 = 50
num2 = 100
if(num1>num2):
    print(num1)
else:
    print(num2)
# 절대값 구하기
if(num1>num2):
    dif = num1 - num2
    print(dif)
else:
    dif = num2 - num1
    print(dif)







