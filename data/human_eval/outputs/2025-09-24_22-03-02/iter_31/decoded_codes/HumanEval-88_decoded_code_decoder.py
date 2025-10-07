def sort_ascending(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort

def sort_descending(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] < list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort

def sort_array(array):
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    is_sum_even = (sum_first_last % 2) == 0
    array_copy = [elem for elem in array]
    if is_sum_even:
        return sort_descending(array_copy)
    else:
        return sort_ascending(array_copy)