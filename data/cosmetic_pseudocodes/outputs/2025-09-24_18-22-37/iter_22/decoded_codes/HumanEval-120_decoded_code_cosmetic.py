from typing import List

def maximum(numbers_collection: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    temp_sort_var: List[int] = numbers_collection[:]
    n: int = len(temp_sort_var)
    for i in range(1, n):
        for j in range(n - i):
            if temp_sort_var[j] > temp_sort_var[j + 1]:
                temp_sort_var[j], temp_sort_var[j + 1] = temp_sort_var[j + 1], temp_sort_var[j]
    slice_start_index: int = n - count_positive
    result_list: List[int] = []
    current_index: int = slice_start_index
    while current_index < n:
        result_list.append(temp_sort_var[current_index])
        current_index += 1
    return result_list