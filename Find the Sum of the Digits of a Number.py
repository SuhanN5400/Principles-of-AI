def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = 12345
print("Sum of the digits of", num, "is", sum_of_digits(num))
