print()
'''
# exception 다루는 방법
1) 예외를 잡는 방법
2) 파이썬에 미리 정의되어 있는 예외를 일으키는 방법
'''

# value = '가'
#
# try:
#     if value not in ['A', 'B', 'C']:
#         raise ValueError('알파벳 중 하나이어야 합니다')
# except ValueError:
#     print('오류가 발생했음')

print('------------------------------------------')
'''
# 코드가 복잡해지고 함수를 여러번 호출하게 되면 오류를 낼 수 있는 코드도 많아지게 됨
  더해서 어디에선가는 잡지 말아야할 오류를 잡게되어버린다면 전체 코드 진행이 의도한대로 되지 않을 가능성도 있어짐
  또 이미 처리해버린 오류가 실제 어디서 발행했는지 알아내는 것은 처리 하지 않은 오류가 어디서 발생했는지 
  알아내는 것보다 훨씬 더 번거로움
 
# 이런 다양한 문제들을 처리하기 위해 파이썬도 프로젝트에 맞게 예외를 하나의 클래스(사용자 정의)로 만들어서
  직접 새 예외를 만들 수 있음
'''
# from 구문 후 호출할 파이썬 모듈이 안보일 경우: source root 처리
from exceptionObject import Unexpected_exep

value = '가'

try:
    if value not in ['A', 'B', 'C']:
        raise Unexpected_exep
except Unexpected_exep:
    print('오류가 발생했음')

'''
# 사용자 정의를 이용한 exception 처리 결과는 일반 오류처리 결과와 섞이지 않고
  모두 처리해 주는것을 확인할 수 있음 
'''