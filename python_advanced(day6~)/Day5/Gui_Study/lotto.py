import random  # 랜덤으로 받아오기위해 선언
def make_lotto():  # 함수 정의
    lotto_num = set()  # 중복값을 허용하지 않는 set 으로 설정

    while len(lotto_num) < 6:  # while 문으로 6자리 숫자 0,1,2,3,4,5  까지 반복 실행
        number = random.randint(1,45)  # 랜덤으로 받는 수는 정수(randint) 1~45 까지 생성
        lotto_num.add(number)  ## set 의 자료 안에 생성된 자료형 추가
    return lotto_num  ## 리턴값으로 최종적으로 생성된 랜덤 로또 수를 저장
# input : n (생성 수), output : list( 로또 리스트)

def lotto_maker(n):
    lotto_list = []
    for i in range(n):
        lotto_list.append(make_lotto())
    return lotto_list
if __name__ == "__main__":

    print(lotto_maker(10))
else:
    print("import 해서 사용하는군!")
