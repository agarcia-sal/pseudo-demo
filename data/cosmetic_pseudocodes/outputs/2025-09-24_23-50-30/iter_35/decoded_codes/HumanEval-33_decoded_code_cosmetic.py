from typing import List, TypeVar

T = TypeVar('T')


def sort_third(array_arg: List[T]) -> List[T]:
    temp_array: List[T] = []
    idx = 0
    while idx < len(array_arg):
        if (idx % 3) == 0:
            temp_array.append(array_arg[idx])
        idx += 1

    n = len(temp_array)
    i = 1
    while i < n:
        j = i
        while j > 0 and temp_array[j - 1] > temp_array[j]:
            temp_array[j], temp_array[j - 1] = temp_array[j - 1], temp_array[j]
            j -= 1
        i += 1

    k = 0
    m = 0
    result_copy: List[T] = [element for element in array_arg]

    while m < len(result_copy):
        if (m % 3) == 0:
            result_copy[m] = temp_array[k]
            k += 1
        m += 1

    return result_copy