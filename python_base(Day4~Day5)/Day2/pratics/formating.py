#문자열 포맷팅- 입력값에 따라 달라지는 상항에 매핑을 하는것


#1. form선언후 해당 변수 선언후 출력하는 방법
#"사람들 마다 각기 다른 치수를 입력 받아 출력하는 프로그램을 찌보자"
# %d, %f, %s 연산자를 사용!- 타입이 다르기떄문

# %d = 상수를 나타냄
form = "제 나이는 %d 살 입니다"
boy1 = form % 24
boy2 = form % 26

print(boy1)
print(boy2)


# %f = 실수를 나타냄
# 자릿수를 나타내는 경우 %뒤에 .과 나타내고싶은 자릿수를 표기(반올림하여 표기됨)
form = "제 영어성적은 %.2f점 입니다 "
boy3 = form % 78.529
boy4 = form % 95.4

print(boy3)
print(boy4)

#%s = 문자를 나타냄
form = " 나의 이름은 %s 입니다"
boy5 = form % "다니엘"
boy6 = form % "민지"
print(boy5)
print(boy6)

#example
a = input("나이를 입력하세요:")
b = input("이름을 입력하세요:")

print("My name is %d and my age is %s years old." % (int(b),a))

# 2.str.format함수 사용하는 법
name = "Alice"
age = 25
print("My name is {0} and I am {1} years old.".format(name,age))

# 3. F-string 사용 방법
print(f"My name is {name} and My age is {age} years old")

#input 과 응용
kg = input("오늘 점심은:")
cm = input("오늘 인원은:")
print(f"오늘의 점심메뉴는 {kg} (이)며, 오늘의 인원은 {int(cm)}명 입니다")
