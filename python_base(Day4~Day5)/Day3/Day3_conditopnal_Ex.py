# 사용자로부터 성적과 봉사활동 시간을 입력받아 장학금 지급여부를 판단합니다.
# 조건1 : 학점3.5이상
# 조건2 : 봉사활동 50시간 초과<--이상과 초과는 다름.

grade = float(input("성적을 입력하세요 : ")) ## 3.5 이기에 float 로 타입 설정

if grade >= 3.5:

    vol = int(input("봉사활동 시간을 입력하세요 : "))
    if vol > 50:
        print("장학금 지급 대상입니다")
    else:
        print("봉사활동 점수가 부족합니다")
else:
    print("학점이 부족합니다")
print("종료")


# st1 = float(input("값 : "))
# cir = str(input("연산자 : "))
# st2 = float(input("값 : "))

# if cir == "+":
#     print(st1 + st2)
# elif cir == "-":
#     print(st1 - st2)
# elif cir == "*":
#     print(st1 * st2)
# elif cir == "/":
#     print(st1/st2)

