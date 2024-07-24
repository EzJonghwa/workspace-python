
gender = input("성별은?:")
age = int(input("나이는?"))
#남자이면서 10설 이상만
if gender == "남" and age >= 10:
    print("적합합니다")
else:
    print("부 적합 합니다.")

email = "jj2bae@naver.com"
if "@" in email:
    print("이메일 형식입니다.")
else:
    print("이메일 형식이 아닙니다.")