# # 함수에 대하여
# #def 를 사용해서 선언
# def adder (a,b): ## 인스(파라미터)
#     sum = a+b
#     return sum #// 덧셈값 리턴
# # 매개 변수외 리턴값은 없을 수도 있음
# # 예시 : 
# def test():
#     print("매개변수와 리턴 값이 없음")

# print(adder(1,10))
# m= adder (10,2)
# print(m)
# n= adder(int(input("덧셈할 값")),int(input("덧셈할 값")))
# print(n)

# # return 값 == 0 ~n개 가능
# def fn_name():
#     return 10 ,100
# a ,b = fn_name()
# print(a,b) 
# # 10 100

# #디폴트 매개변수 
# def fn_default(nm, leverl=1):
#     print(f"이름 :{nm} 레벨:{leverl}")
# fn_default("nick")
# fn_default("jack", 100)

# 가변형 매개변수 (0~n)개
# + 더하기 , * 곱하기 연산 후 리턴
def fn_calculator(operator,*args):
    result = 0
    if operator == "+":
        for n in args:
            result += n
    else:
        result = 1
        for n in args:
            result *= n
    return result
print(fn_calculator("+",1,2,3))
print(fn_calculator("*",10,2))