import os
# os 는 파이썬의 표준 라이브로 운영체제어 상호작용하는 다양한 기능을 제공
# 파일 시스템 탐색 및 삭제, 변경 , 생성...
print(os.getcwd) #파일의 현재위치
dir = os.getcwd()
file_list = os.listdir(dir) # 현재 위치의 모든 파일 리스트
print(file_list)
del_file_path = os.path.join(dir, file_list[0])
print(del_file_path)
os.remove(del_file_path) 
## 휴지통에 들어기지 않음 , rmdir : 폴더 삭제
