from collections import Counter

def find_mode(lst):
    counter = Counter(lst)
    max_count = max(counter.values())
    mode = [key for key, count in counter.items() if count == max_count]
    return mode

my_list = [1, 2, 2, 3, 3, 3, 4]
print("Mode of the list:", find_mode(my_list))
