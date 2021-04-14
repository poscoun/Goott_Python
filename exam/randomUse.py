print()
list = ['빨', '주', '노', '초', '파', '남', '보']

'''
# 1. 공식문서에서 random 모듈을 검색하여 list 중 하나를 랜덤하게 갖도록 만들어보기
# 2. 공식문서에서 random 모듈을 검색하여 random_number 가 2이상 10이하의 랜덤한 정수를 갖도록 해보기
# 3. 공식문서에서 random 모듈을 검색하여 list를 모두 섞어보세요
# 4. lotto 6자리 구현해보세요.
'''

# 1. 공식문서에서 random 모듈을 검색하여 list 중 하나를 랜덤하게 갖도록 만들어보기
import random
print(random.choice(list))  # choice() : 아무 원소 하나를 뽑아준다.

# 2. 공식문서에서 random 모듈을 검색하여 random_number 가 2이상 10이하의 랜덤한 정수를 갖도록 해보기
print(random.randrange(2, 11))      # randrange(x, y) : x 이상 y 미만의 난수

# 3. 공식문서에서 random 모듈을 검색하여 list를 모두 섞어보세요
random.shuffle(list)        # shuffle() : 순서형 자료(sequence)를 뒤죽박죽으로 섞어놓는 함수
print(list)

# 4. lotto 6자리 구현해보세요.
result = []
while len(result) < 6:
    num = random.randrange(1, 45)     # 1부터 45까지의 난수 발생
    if num not in result:             # result 리스트 안에 num이 없으면 아래의 문장을 실행
        result.append(num)

print(result)