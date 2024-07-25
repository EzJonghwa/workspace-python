def sum_ofsquares(numbers):
    total = 0
    for number in numbers:
        total += number **2
    return total
number = [1,2,3,4,5]
result = sum_ofsquares(number)
print("sum if squares :", result)