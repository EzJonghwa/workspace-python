'''
    파이썬에서 예외 처리는 프로그램이 실행되는 도중 발생할 수있는 오류입니다. 
    예외상황을 관리하는 방법.
    "try" 블록에서 오류가 발생하면 해당 오류를 "except" 블록에서 잡이ㅏ 처리 할 수있음
'''

## 기본구조
# print("프로그램 시작")
# try:
#     print("1")
#     result = 10 / 0   #<---------------------
#     print("2")                             #| 이동 print2 는 스킵됨
# except ZeroDivisionError as e:  #<-----------
#     print(f"예외가 발생 하였습니다. : {e}")
# print("프로그램 종료")
# # 오류처리를 하는것이 중요 (중도 종료 되지 않게)

def test(value):
    sum = 0
    try:                            # 기본로직이 실행되는 부분
        sum = value[0] + value[1]
        sum /0
    except IndentationError as e:
        print(f"인덱스 에러 구간 : {e}") #인덱스 오류만
    except Exception as e:
        print(f"모든 err : {e}")    # 모든 에러 상황

    else:
        print("에러 없음 ")         # 에러가 없을 떄만 실행됨
    finally:
        print(sum)                 # 정상, 오류가 모두 실행되는 부분


test([True, True])