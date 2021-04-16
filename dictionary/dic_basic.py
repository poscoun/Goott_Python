print()
'''
# dictionary
 : {name1 : value1, name2 : value2, ...}
'''
wager = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

print(wager['보'])

# 가위, 바위, 보 승패판정 함수 생성해보세요
def rsp(x, y):   # 내가 낸 것은 x, 남이 낸 것은 y
    if x == y:
        return '비김'
    elif wager[x] == y:
        return '이김'
    else:
        return '졌음'


result = rsp('가위', '바위')
print(result)

print('-----------------------------------------------')
# name에는 리스트를 사용할 수 없지만 값에는 리스트를 사용할 수 있다.
dic = {
    'tag' : [1,2,3]
}

print(dic)