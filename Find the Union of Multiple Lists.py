def union(*lists):
    return list(set().union(*lists))

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
print("Union of lists:", union(list1, list2, list3))
