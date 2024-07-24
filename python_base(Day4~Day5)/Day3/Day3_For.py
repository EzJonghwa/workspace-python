
# for 문은 반복적으로 코드를 실행하는데 사용됨
# 코드의 중복을 줄이고, 효율성을 높이며 데이터 집합을 처리하기 위함.

#방법1 기본 for 문 : 시퀀스(list, tuple ,str)의 각 요소를 순회하면서실행
#리스트 순회
nums = [1,2,3,4,5]
for num in nums:
    print(num)
print("=" * 10)
world = "hello" #문자열 또한 인덱스가 있는데이터 이기 떄문에 순차적으로 출력 가능
for letter in world:
    print(letter)
print("=" * 10)


# 방법2 단순 반복range(cnt) 일정범위로 반복
# 0~4 숫자 순호ㅣ
for i in range(5):
    print(i)
print("=" * 10)
# 1~5 까지
for i in range(1,6):
    print(i)
print("=" * 10)
# 1~10 까지 2 씩 증가하며
for i in range(1,11,2):
    print(i)

# 방법3 enumerate() 인덱스와 값이 동시에 필요할 떄
for idx, val in enumerate(nums):
    print(f"index:{idx} value:{val}")
            # index:0 value:1
            # index:1 value:2
            # index:2 value:3
            # index:3 value:4
            # index:4 value:5

# 구구단 출력하기
dan = int(input("단을 입력하세요 :"))
for i in range(1,10):
    print(f"{dan} x {i} = {dan * i}")

# 중첩 for 문 (for  문 안에for 문)
for d in range(2,10):
    print(f"=========================== {d}단 ===========================")
    for j in range(1,10):
        print(f"{d} x {j} = {d * j}")