print()
'''
# 특정 함수나 클래스만 불러오기
# from <모듈이름> import <함수이름>
'''

# calculator 모듈의 add() 만 호출
from calculator import add

print(add(100, 100))

# calculator 모둘의 모든 메소드 사용
from calculator import *

print(add(100, 200))
print(mul(100, 200))
print(div(200, 100))

print('--------------------------------------------------')
# 모듈을 다른 이름으로 호출 (별칭) - 사용하려는 모듈이 이름이 너무 긴 경우
# ex) tensorflow -> tf, pandas -> pd, numpy -> np, matplotlib - plt
import thisisVeryLongNameModule as t

t.hello()
