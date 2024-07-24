# 문자열 관련 함수
print("hello".find("e")) # 특정 문자열의 인덱스값 찾기
print("     hello     ".strip()) # 공백을 제거함 lstrip = 좌측 공백 제거/ rstrip = 우측 공백 제거
print("     hello     ".rstrip()) # 공백을 제거함 lstrip = 좌측 공백 제거/ rstrip = 우측 공백 제거
arr = "hello world".split() # 구분 문자를 기분으로 분자열을 자름(구분기호 자르기)
print(arr)
email = "jj2bae@naver.com".split("@")
print(email)

print("hello world".replace("world" , "Python")) # 변경하기

#사용자에게 문장을 입력받아 줄이말을 만들어 주세요
# 갑자기 분위기 싸함
# 갑 분 싸

word = input("문자를 입력하세요 :").split()
print(word)
for i in word:
    print(i)


