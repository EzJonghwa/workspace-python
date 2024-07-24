milk_brand = ["서울", "부산", "파스퇴르"]
milk_price = [1400,1500,1800]
milk_recipt = ["원산지 : 강릉 납품 : 경기도","원산지 : 대구 납품 : 경상도", "원산지 : 대전 납품 : 충청도"]


print(milk_price)
for mb, mp, mr in zip(milk_brand,milk_price,milk_recipt):
    print(f"{mb}의 가격:{mp} 정보:{mr} ")