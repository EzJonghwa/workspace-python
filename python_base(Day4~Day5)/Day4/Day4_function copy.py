#로또를 생성하고 리턴하는 함수를 작성
#함수명 meke_lotto
#매개변수 x
#리턴 set 자료형태 (로또번호)
# (랜덤, 셋 , 렝스 )

def make_lotto():  # 함수 정의
    import random  # 랜덤으로 받아오기위해 선언
    lotto_num = set()  # 중복값을 허용하지 않는 set 으로 설정

    while len(lotto_num) < 6:  # while 문으로 6자리 숫자 0,1,2,3,4,5  까지 반복 실행
        number = random.randint(1,45)  # 랜덤으로 받는 수는 정수(randint) 1~45 까지 생성
        lotto_num.add(number)  ## set 의 자료 안에 생성된 자료형 추가
    return lotto_num  ## 리턴값으로 최종적으로 생성된 랜덤 로또 수를 저장

lotto = make_lotto() ## 힘수호츌
print(f"로또 번호는 : {lotto}")    ##함수출력
