def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()
    for number in arr:
        complement = target_sum - number
        if complement in seen:
            pairs.append((complement, number))
        seen.add(number)
    return pairs

arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
pairs = find_pairs_with_sum(arr, target_sum)
print("Pairs with sum", target_sum, ":", pairs)
