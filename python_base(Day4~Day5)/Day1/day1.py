#print 출력 관련
print('test')
# 주석은 코드 실행에 영향을 주지 않음 
# commet 주석 단축키 cntrl + /

# 파이썬은 들여쓰기를 하지 않으면 오류남
if True:
    print ('h1')


# DATA type (자료형)
# 숫자형(numberic tye) 정수(int) 상수(float)
print (10)
# type 함수는 해당데이터의 타입을 반환함
print (type(3.14))


# 산술연산자를 통해 사칙연산이 가능하다
#  + - * /
# % 나머지 반환
# // 몫 반환
# ** 제곱을 반환
print ('나머지:', 12%5)
# 나머지 값을 통해서 짝수 홀수 판별 가능
# python : 출려하고자 하는 값과 데이터 타입이 달라도 콤마 하나로 한번에 다양하게 출력이 가능하다
print('몫 :', 16//2)
print ('제곱 :', 2**4)

# // 문자열// #
# 문자열의 특징
print('가나다'+'라마바사')   #문자열 덧셈 가능
print('h1\n' * 10)           #문자열 굽셈 가능
# 문자열의 타입은 "str"
print(type('h1'))
print("tom's ipad") # 쌍따음표로 선언시 작은 따음표 사용가능 
print('"nick name : boyy"') # 작은따음표로 선언시 쌍따음표 사용가능 
# 문자열의 공백또한 1바이트를 차지한다

# 변수(변할 수 있는수)
abc = 57 # abc 는 57이다 = 자동으로 상수임을 인식
abcd = "57" # abcd 는 57 이다 = ""를 사용한 숫자는 문자로 인식가능
print(type(abc))
print(type(abcd))

# ....변수 명명규칙....#
# 문자 숫자 밑줄만 포함
# 공백 포함 불가
# 첫글자로 숫자 불가
# 폴더명은 보통 영어로 사용하고 숫자는 마지막에!
# 변수(vauable,var) 데이터에 붙이는 이름표
# python 변수의 특징 : 동적타입(변수 타입을 명시하지 않아도 인식함)

my_num = 3
print(my_num, type(my_num))

my_num = 3.14 # 재 할당 또한 가능 "float"
print(my_num, type(my_num))

my_num = "3.14" # 재 할당 또한 가능 "str"
print(my_num, type(my_num))
# 데이터의 형태를 변환 해야 할때 타입 변경이 가능하다
# int, float, str to int(), flaot(), str()
my_num = float(my_num)
print(type(my_num))

# mynameisjeon =  26
# my_name_is_jeon26 = "man"
# print("His age is:",mynameisjeon)
# print("His s is:",my_name_is_jeon26)


#input 핰수 - 사용자에게 입력값을 받기 위해 사용함
a = 3
b = input("숫자를 입력하세요 :") #입력받은 값은 무조건 str로 들어오기에 연산필요시 타입변환 필요
print(a + int(b))
# 이러한 기능을 통해 계산기 코드를 작성 할 수 있음