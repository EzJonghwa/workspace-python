#로또 번호생성
# 1~45의 번호 중 중복되지 않응 6개의 숫자
# 랜덤하게 자동 생성

import random
lotto_num = set() # 번 set선언 "중복 되지 않은 값 선언시 SET 사용"
# set 의 길이기 6이 될 때 까지 <6
# # 문자열의 길이나 시퀀스 자료형의 길이를 리턴하는 함수 len() , 자료형의 갯수 또한 출력 가능
# print(len('abc')) ## 길이는 3
# kk = [1,2,3,4] ## 갯수는 4
# print(len(kk))
while len(lotto_num) < 6:
    number = random.randint(1,45)
    lotto_num.add(number)
print(f"행운의 로또 번호 : {lotto_num}") 
# 출력 : 행운의 로또 번호 : {3, 42, 44, 16, 25, 27}

#사용자에게 입력받은 수 만큼 로또 번호생성
import random

cnt = int(input("원하시는 수를 입력하세요 : "))
for i in range(cnt):
    lotto_custom = set() 
    # for 안에 넣어야지 새로 돌면서 랜덤한 숫자가 생성 만약 for 문 위에 넣으면 같은 수 반복출력 (반복하면서 새로워지지 않기에)
    while len(lotto_custom) < 6:
        number = random.randint(1,45)
        lotto_custom.add(number)
    print(f"행운의 로또 번호 : {lotto_custom}") 
