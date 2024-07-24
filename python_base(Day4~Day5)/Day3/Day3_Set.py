# set 중복을 허용하지않음
my_set = {1,2,2,3,4,4,5} ## 중복값 제거됨
print(my_set)

# 요소추가
my_set.add(6)
my_set.add(6) ## 중복값을 추가해도 하나밖에 안들어간다
print(my_set)
# 여러 데이터 추가
my_set.update([7,8,9])
# 요소삭제
my_set.remove(1)
print(my_set)
# 전체 삭제
my_set.clear()
# 집합 연산
set1 = {"apple" ,"banana"}
set2 = {"banana", "watermelon"}

inter =  set1 & set2 ## 교집합
print(inter)

uni = set1 | set2 #합집합
print(uni)

diff =  set1 - set2 # 차집합
print(diff)
diff2 = set2 - set1 # 차칩합
print(diff2)