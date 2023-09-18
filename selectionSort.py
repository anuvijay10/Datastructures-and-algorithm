# arr = [64, 25, 12, 22, 11]
# arr = [65, 64, 63, 62, 61]
# arr = [1, 5, 3, 9, 6, 6]
# arr = [25,12,65,22,11]
# arr = [1, 2, 3, 4, 5, 6]
# arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]

arr = [99, 65, 64, 0, 25, -1, 12, 22, 11, -1]
for i in range(0, len(arr) - 1):
    min_index = i  # Taking first index as mid index
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)

