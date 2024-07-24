import requests

api_url = "https://open.er-api.com/v6/latest/USD" # 클라이언트로 써 페이지에 요청 (openapi) jason 데이터로 들어옴

response = requests.get(api_url) # get으로 받아옴

print(response.text) # 텍스트데이터 받아오기
data = response.json()

# # print(data['rates'])
# print(data['rates']['KRW'])
# # 딕셔너리 데이터에서 키 값만 가져오는 함수다
# for key in data['rates'].keys():
#     print(f"{key}:{data['rates'][key]}")
usd_to_krw = data['rates']['KRW']

while True:
    msg = input("달러를 입력하세요(종료:q) : ")
    if msg == "q":
        break
    amount_usd = int(msg)
    amount_krw = amount_usd * int(usd_to_krw)
    print(f"{amount_usd}$ 는 한국돈으로 {amount_krw:,}원 입니다.") # :, 천단위 컴마 추가하기

## pyinstaller --onefile --console Day5_Requests.py
# pyinstaller --onefile --console --hidden-import=ssl day5_requests.py