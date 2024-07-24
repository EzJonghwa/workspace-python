# 할인 퍼센트와 물품의 금액을 입력받아
# 할인 금액과 최종금액을 계산하여
# 출력하는 프로그램을 작성하시오

#사용자로부터의 입력
original_price = float(input("상품 금액:"))
dis_percent = float(input("할인 퍼센트(ex 20% = 20 입력):"))

# 할인금액 계산
discounnt_amount = original_price * (dis_percent / 100)

# 최종 금액 계산
final_price= original_price -discounnt_amount

# 결과 출력
#... f-string 에서 자릿값 표현시 :.자릿수 입력하기
print(f"원가:{original_price}원")
print(f"할인률:{dis_percent:.2f}%")
print(f"할인금액:{discounnt_amount:.2f}원")
print(f"최종금액:{final_price:.2f}원")



