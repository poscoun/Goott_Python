import math

# 둘레 구하기 : r * 2 * 3.14
r = 10

print(r * 2 * math.pi)

# 올림 : ceil
print(math.ceil(2.4))

# 내림 : floor
print(math.floor(4.7))

# 반올림
# print(math.round(3.5))     
print(round(3.5))   # round() : 자주 사용하는 함수여서 내장함수에 있음

# 이 밖에도 삼각함수, 지수, 승, 로그 등 다양한 기능이 math에 있음

print('------------------------------------------------------------')
import sys

print(sys.argv)
print(sys.path)

print('-------------------------------------------------------------')
import os

# 시스템의 환경변수값 확인
print(os.environ)

print(os.environ['Path'])

# 디렉토리 변경
# os.chdir('goott_python')
print(os.getcwd())

os.system('dir')
'''
# 그 외 os 모듈
os.popen : 시스템 명령어를 수행한 결과값을 읽기모드의 파일 객체로 리턴
os.mkdir(디렉토리명) : 디렉토리 생성
os.rmdir(디텍토리명) : 디렉토리 삭제 (주의 - 디렉토리가 비어있어야 함)
os.unlink(파일명) : 파일 삭제
os.rename(src, dst) : src 이름 파일을 dst 이름으로 변경
'''
# os.mrdir('testDir')
# os.rmdir('testDir')

print('-----------------------------------------------------')
import shutil
'''
shutil.copy(src, dst) : src라는 이름의 파일을 dst로 복사
'''
shutil.copy('moduleEx01.py', 'moduleEx01_test.py')