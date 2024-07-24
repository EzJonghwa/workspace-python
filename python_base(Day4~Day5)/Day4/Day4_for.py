# 2차원 리스트 순회
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix: # 매트릭스 변수 안에 있는 
    print(row)
    for element in row: # row  안에 존재하는 element들
        print(element)

#두 리스트 병렬 순회
names = ['nick', 'jakck', 'alice']
score = [85,90,95]
for nm, num in zip(names, score):
    print(f"{nm}의 성적은 {num}점")

for idx ,val in enumerate(names):
    print(f"{val} : {score[idx]}")

milk_brand = ["서울", "부산", "파스퇴르"]

#dict 키를 이용한 for문(순서가 아닌 키 값으로 불러오기에)
#dict 함수중에 .keys()함수를 사용하면 key값을 불러 올 수 있다
stu = {"kokk" : 40, "jarki" : 60, "anemy" : 50}
print(stu.keys())
for key in stu.keys():
    print(stu[key]) #40 60 50 출력

#items() 함수
for key, val in stu.items():
    print(f"{key}:val")