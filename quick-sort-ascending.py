def pivot_position(list1, first, last):
    pivot = list1[last]
    left = first
    right = last
    for i in range(left, right):
        if list1[i] <= pivot:
            list1[i], list1[left] = list1[left], list1[i]
            left += 1
    list1[left], list1[last] = list1[last], list1[left]
    return left


def quicksort(list1, first, last):
    if first < last:
        pi = pivot_position(list1, first, last)
        quicksort(list1, first, pi - 1)
        quicksort(list1, pi + 1, last)


# Example usage:
my_list = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# my_list = [-2, 1, 5, 0, 1, 2]
n = len(my_list)
quicksort(my_list, 0, n - 1)
print(my_list)
