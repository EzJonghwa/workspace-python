# #문자열 포맷팅 
# 문자열유형의 서식 데이터를 만들고, 서식안에 데이터를 대입하는 방법
# 방법1 기본 포매팅(%연산자 사용)

nm = "nick"
age = 38
formatted_str ="my name is %s and i am %d year old"% (nm,age)
print (formatted_str)

num =123.4566789
formatted_str2 = "The number is %.2f" % num
print(formatted_str2)

#방법2. str,format() 함수 사용
formatted_str3 = "my name is {0} and i am {1} year old" .format(nm,age)
print(formatted_str3)

#방법3.(f.string ) 파이썬 3.6이사에서 사용가능
print(f"my name is {nm} and i am {age} year old")