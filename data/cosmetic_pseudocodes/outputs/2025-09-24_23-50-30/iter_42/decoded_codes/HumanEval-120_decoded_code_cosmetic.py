from typing import List


def maximum(list_of_numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    array_sort_nondecreasing(list_of_numbers, 0, len(list_of_numbers) - 1)
    start_index = len(list_of_numbers) - count
    return sublist_extract(list_of_numbers, start_index, len(list_of_numbers))


def array_sort_nondecreasing(arr: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    pivot_value = arr[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot_value:
            i += 1
        while arr[j] > pivot_value:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    array_sort_nondecreasing(arr, left, j)
    array_sort_nondecreasing(arr, i, right)


def sublist_extract(source: List[int], from_index: int, to_index: int) -> List[int]:
    result = []
    index_var = from_index
    while index_var < to_index:
        result.append(source[index_var])
        index_var += 1
    return result