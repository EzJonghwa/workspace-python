#입력받기
msg= input("문장을 입력하세요 : ").split() 
print(msg)

message = ""
for i in msg:
    message += i[0]
#반복하기 ( 메세지 조합 )
print(message)
#출력

def solution(angle):
    if int(angle) == 180:
        answer = 4
    return answer
print("answer")