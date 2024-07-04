def rotate_list(arr, steps):
    steps = steps % len(arr)
    return arr[-steps:] + arr[:-steps]

arr = [1, 2, 3, 4, 5]
steps = 2
rotated_list = rotate_list(arr, steps)
print("Rotated list:", rotated_list)
