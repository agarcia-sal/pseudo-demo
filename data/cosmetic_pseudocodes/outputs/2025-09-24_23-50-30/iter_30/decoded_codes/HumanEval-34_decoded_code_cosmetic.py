from typing import List, TypeVar

T = TypeVar('T')

def unique(array_items: List[T]) -> List[T]:
    temp_set: set[T] = set()
    for elem in array_items:
        temp_set |= {elem}

    result_list: List[T] = []
    for val in temp_set:
        result_list.append(val)

    n: int = len(result_list)
    i: int = 0
    while i < n - 1:
        j: int = i + 1
        while j < n:
            if result_list[j] < result_list[i]:
                result_list[i], result_list[j] = result_list[j], result_list[i]
            j += 1
        i += 1

    return result_list