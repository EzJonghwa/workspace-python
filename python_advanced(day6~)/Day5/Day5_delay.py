# open함수는 파일을 읽고 쓸 수 있는 함수.
# "a"ppend , "r"ead , "w"rite
f = open("delay.txt", "a", encoding="utf8") # 한글 인코딩 설정 "utf8" 
f.write("오늘의 지각자!\n") # Write : 파일에 쓸 때 \n :이스케이프문자
while True:
    n = input("오늘 지각한 사람!!!(q, 종료) : ")
    if "q" == n:
        break
    f.write(n)
    f.writelines('\n')
f.close()
