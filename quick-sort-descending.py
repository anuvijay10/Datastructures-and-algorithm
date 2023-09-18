def pivot_position(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last

    while left <= right and list1[left] >= pivot:
        left += 1
    while left <= right and list1[right] <= pivot:
        right -= 1
    if left > right:
        list1[first], list1[right] = list1[right], list1[first]
    else:
        list1[left], list1[right] = list1[right], list1[left]

    return right


def quicksort(list1, first, last):
    if first < last:
        pi = pivot_position(list1, first, last)
        quicksort(list1, first, pi - 1)
        quicksort(list1, pi + 1, last)


# Example usage:
# my_list = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
my_list = [-2, -1, 0, 1, 2]
n = len(my_list)
quicksort(my_list, 0, n - 1)
print(my_list)
