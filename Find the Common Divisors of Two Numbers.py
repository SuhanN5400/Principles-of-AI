def common_divisors(a, b):
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

num1 = 12
num2 = 18
print("Common divisors of", num1, "and", num2, ":", common_divisors(num1, num2))
