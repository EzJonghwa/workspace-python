#with 룰 쓰면 꼭 단기를 하지 않아도 사용이 끝나면 닫아줌
with open("delay.txt", "r", encoding="utf8") as f:
    for line in f: # 라인단위로 읽어오는 함수
        print(line.strip()) # 공백제거하기위한 함수