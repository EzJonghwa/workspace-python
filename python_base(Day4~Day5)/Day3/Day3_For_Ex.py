# python 에서 import 문은 다른 모듈이나 라이브러리를 
# 현재 파이썬 프로그램으로 가져와 사용 할 수있게 함.
import random
# 랜덤으로 값을 생성하는 모듈

#0.0에서 1.0 사이의 난수(float)를 반환
print(random.random())
#randint (a,b) 사이의 정수를 랜덤하게 변환
print(random.randint(1,45))
#구구단 게임  랜덤 구구단 문제를 주고 사용자 입력값이 맞으면 "정답", 틀리면 "오답" 출력


# #문제출력
for i in range(1,11):
    dan = random.randint(2,9) # 2~9 사이의 랜덤값
    num = random.randint(1,9) # 1~9 사이의 랜덤값
    print(f"{dan} x {num} == ?")
    ans = dan * num
    if ans == int(input("답을 입력하세요 :")):
        print("정답입니다.")
    else:
        print(f"오답입니다..정답은 {ans}입니다")
print('게임을 종료합니다.')
