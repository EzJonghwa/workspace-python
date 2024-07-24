# orginal= input("주민번호 입력하세요(- 포함):")
# fi_original = orginal.find('-')
# select = orginal[fi_original+1]

# if  select == 1 or select == 3:
#     print("남성입니다")
# elif  select == 2:
#     print("여성입니다")


#사용자로부터 주민번호를 입력받아
#여자일 경우 대상자입니다 출력
#남성일 경우 대상자가 아닙니다를 출력 하기
id_num = input("주민번호 입력하세요(- 포함):")
# 1.문자열 인덱스로 마지막자리 가져오기
id_num_se = id_num.find('-')
id_num_xx = int(id_num[id_num_se+1])


if id_num_xx == 1 or id_num_xx ==3:
    print("대상자가 아닙니다")
# elif id_num_xx == 3:
#     print("대상자가 아닙니다")
else:
    print("대상자 입니다")

# 2. 산술 연산자를 통해 성별 가져오기
# 3. 조건문 if 를 이용하여 출력
## % 2 == 0 짝수 홀수 구분으로도 프로그램을 작성할 수있다.