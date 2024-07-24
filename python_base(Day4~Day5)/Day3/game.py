import random
while True:
    dan = random.randint(2,9) # 2~9 사이의 랜덤값
    num = random.randint(1,9) # 1~9 사이의 랜덤값
    print(f"{dan} x {num} == ?")
    ans = dan * num
    if ans == int(input("답을 입력하세요 :")):
        print("정답입니다.")
    else:
        print(f"오답입니다..정답은 {ans}입니다")
        break
print('게임을 종료합니다.')
