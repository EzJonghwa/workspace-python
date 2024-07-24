#사용자로 부터 원화 금액을 입력받아
#환율을 계산해서 출력하시오
    # http://open.er-api.com/v6/latest/usd
krw_amount = float(input("원화 금액을 입력하세요(원):"))
exchnge_rate_usd = 1382.09 #현재환율
#원화 금액을 외화로 변환
exchange_money = krw_amount / exchnge_rate_usd
#결과 출력2
print(f"원화금액 {krw_amount}원")
print(f"환율 1달러 당{exchnge_rate_usd}원")
#외화 금액 출력
print(f"환전금액:{exchange_money:.2f}$")

