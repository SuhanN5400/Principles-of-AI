def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

lower = 100
upper = 1000
armstrong_numbers = [num for num in range(lower, upper) if is_armstrong(num)]
print("Armstrong numbers between", lower, "and", upper, "are:", armstrong_numbers)
