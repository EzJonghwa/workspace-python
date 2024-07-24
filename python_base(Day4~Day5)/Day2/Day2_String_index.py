#문자열 인덱싱
#문자열 인덱스는 0부터 시작
text = "Hello world!"
print(text[0]) #H
print(text[3]) #l
print(text[5]) #공백
print(text[8]) #r
print(text[7]) #o
print(text[2]) #l
print(text[1]) #e
print(text[-1]) #! -는 뒤에서부터 접근 가능

# 문자열 슬라이싱
text1 = "python programming"
# [start:end:step] default 1
print(text1[0:15:3]) #0 부터 7까지 3개씩 띄워서
print(text1[0:18]) # 전체
print(text1[7:18]) #programming
print(text1[::2]) #처음부터 끝까지 2칸씩 건너 띄워서
print(text1[::-1]) #역순으로출력한다
print(text1[::-2]) # 뒤에서부터 2칸씩 건너띄워서

#문자열 함수 find(str) 찾고자하는 문자열 str의 인덱스를 반환 없으면 -1 반환
num = "leeapgil@gmail.com"
print(num.find('@'))
