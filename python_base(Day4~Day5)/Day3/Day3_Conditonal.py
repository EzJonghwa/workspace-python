# # 조건문 if 느 조건에 따라 코드 블록을 실행 하거나 실행하지 않도록 제어함
# # 주의사항(들여쓰기,조건식의 순서, none, [], 0 은 false 인식)

# num = int(input('숫자를 입력하세요:'))
# if num > 5:
#     print("입력은 5보다 큼")
# elif num > 7 :
#     print('이부분은 실행되지 않음') ## 조건식의순서상 먼저 만족하는 조건이 있기 때문에 실행되지 않는다
# elif num == 3:
#     print('3이군요!')
# else:       # if의 뒤에는 조건식이 필요하지만 else는 조건식이 필요 x
#     pass # 아무작업을 하지않을때 문법상만들어주는것 (else + pass)
# print('종료')

# 중첩 if문 (if 문 안에 if문)
# 영화관람 체크
# 조건1 : 18세 이상 관람가
# 조건2 : 신분증이 있어야함(있으면:y / 없으면:n)
# ** upper(),lower() = 대문자와 소문자 강제 설정가능 - 내장함수

age = int(input('나이를 입력하세요 :'))
has_id = input('신분증을 소지하고 있나요>(y/n) :'.lower())
if age >= 18:
    if has_id == 'y':
        print("영화 관람이 가능합니다")
    else:
        print("영화 관람이 불 가능합니다")
else:
    print('18세 미만은 입장 할 수 없습니다.')
## if 문은 들여쓰기와 : 로 구분되기에 정확하게 처리할 필요가 있다