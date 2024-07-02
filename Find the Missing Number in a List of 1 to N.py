def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

arr = [1, 2, 4, 5, 6]
n = 6
missing_number = find_missing_number(arr, n)
print("The missing number is", missing_number)
