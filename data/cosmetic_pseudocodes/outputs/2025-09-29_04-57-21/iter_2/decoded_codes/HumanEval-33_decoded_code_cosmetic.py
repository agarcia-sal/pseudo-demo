from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = []
    idx: int = 0
    while idx < len(list_input):
        if idx % 3 == 0:
            temp_list.append(list_input[idx])
        idx += 1

    sorted_subset: List[T] = []
    while temp_list:
        min_val: T = temp_list[0]
        for val in temp_list:
            if val < min_val:
                min_val = val
        sorted_subset.append(min_val)
        temp_list.remove(min_val)

    result_list: List[T] = list_input.copy()
    pos: int = 0
    for i in range(len(result_list)):
        if i % 3 == 0:
            result_list[i] = sorted_subset[pos]
            pos += 1

    return result_list