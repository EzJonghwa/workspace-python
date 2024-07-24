#list(배열)
#동적배열 자유롭게 확장이가능'
#타입에 국한되지 않는다 다양한 타입이 자유로움
arr = [1,'nick', [2,3,[4,5]]]
#인덱스로 요소에 접근
print(arr[0])
print(arr[1]) # nick
print(arr[-1]) # [2,3]
print(type(arr))
print(arr[2][1]) # 2번째 배열의 1번째 == 3
print(arr[2][2][1]) # 2번째 배열의 2번째 배열의 1번째 == 5

#수정하는 법 
arr[1] = 'jack' ## jack으로 수정됨
#추가
arr.append('추가요소') ## 추가시 가장 뒤에 붙음
#제거
del arr[0]
print(arr)
#반복시
repated = arr * 5
print(repated)
#배열의 첫번째는 0 1 2 3

# #배열은 []
# 튜풀은 ()
# 딕셔너리는{}

ar12= [16,13,14,15]
print(ar12)

ar12.append(int(input("추가할 숫자 : ")))
print(ar12)