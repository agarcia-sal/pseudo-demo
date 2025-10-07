from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    first_value = array[0]
    last_index = len(array) - 1
    last_value = array[last_index]
    sum_value = first_value + last_value
    is_sum_even = (sum_value % 2 == 0)
    array_copy = []
    for index in range(last_index + 1):
        array_copy.append(array[index])
    if is_sum_even:
        sort_array_copy_descending(array_copy)
    else:
        sort_array_copy_ascending(array_copy)
    return array_copy

def sort_array_copy_ascending(array_copy: List[int]) -> None:
    n = len(array_copy)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array_copy[j] > array_copy[j + 1]:
                temp = array_copy[j]
                array_copy[j] = array_copy[j + 1]
                array_copy[j + 1] = temp

def sort_array_copy_descending(array_copy: List[int]) -> None:
    n = len(array_copy)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array_copy[j] < array_copy[j + 1]:
                temp = array_copy[j]
                array_copy[j] = array_copy[j + 1]
                array_copy[j + 1] = temp