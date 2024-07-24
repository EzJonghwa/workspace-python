# #반복문 while 조건이 참이면 반복이기에 논리적으로 false 가 없을 시 무한반복
# #조건문에 true 일 경우에만 반복/ false 일 경우 종료
# i = 1
# while i <=5:
#     print(i)
#     i +=1
#     #break 특정 조건일 떄 종료
# print("===================================")
# i = 1
# while True:
#     print(i)
#     if i >= 3:
#         break
#     i +=1
# print("===================================")
# while True:
#     nm = input("이름을 입력하세요(종료: q) : ")
#     if nm == "q":
#         break
#     print(f"{nm}님이 입장하셨습니다.")
# print("종료되었습니다.")
# print("===================================")
# #업다운 게임
# # 1~30 사이의 숫자를 맞춰보세요 총 기회는 3번!
# # 1.1~30 사이의 정수를 랜덤하게 생성
# # 2. 3번의 맟룩 기회를 줌
# # 3. 사용자의 입력이 들어롤 때 마다 맞으면 '정답' 작으면 업 크면 다운 출력
# # 틀릴 때마다 몇번의 기회를 
import random

print("="*20)
print("업 다운 게임")

ran_num = random.randint(1,10)
cnt = 3
while cnt > 0:
    user_num = int(input("정수를 입력하세요 : "))
    #업다운 조건문
    if user_num > ran_num:
        print(" 다운 ")
    elif user_num < ran_num:
        print(" 업 ")
    elif user_num == ran_num: ## else로 해도 무방
        print(" 정답입니다 ")
        break
    cnt -=1
    print(f"남은 기회는 {cnt} 번")
if cnt == 0:
    print(f"기회를 전부 사용하였습니다.. 정답은 {ran_num} ")

