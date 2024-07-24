#학생 성적
score = [85, 90, 65, 100, 75]
#학생 수 :
num_stu =len(score)
print(f"학생 수는 : {num_stu}")
#가장 높은 점수는
max_score = max(score)
print(f"가장 높은 점수 : {max_score}")
#가장 낮은 점수는 
min_score = min(score)
print(f"가장 낮은 점수는 : {min_score}")
# 전체 평균은
avg_score = sum(score) / num_stu
print(f"전체 평균은 : {avg_score}")
# 정렬하기 
sorted_score = sorted(score)
print(score)
print(f"정렬 : {sorted_score}")
#역순으로 정렬
reversed_score = sorted(score,reverse=True)
print(f"역순 : {reversed_score}")


