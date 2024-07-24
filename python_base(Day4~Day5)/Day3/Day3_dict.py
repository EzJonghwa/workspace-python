# 딕셔너리 key -value
# 배열과 마찬가지로 타입에 제한이 없다.
person = {"nm" : "nick", "age" : 20}
# 요소접근은  key로
print(person["nm"]) ## nick 출력
# 요소 수정도 key를 사용
person["nm"] = "jack"
print(person["nm"])
# 요소 삭제또한 key를 사용
del person["nm"]
print(person)
print(type(person))

#학생정보
stu = [{"nm2" : "펭수", "age2" : 10},
       {"nm2" : "명수", "age2" : 20},
       {"nm2" : "갓수", "age2" : 30},
       {"nm2" : "반수", "age2" : 40},
       {"nm2" : "재수", "age2" : 50}]
print(stu)
print(stu[0])
print(stu[2]["age2"])

for i in stu:
    print(i)