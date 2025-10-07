from typing import TypeVar, List

T = TypeVar('T')

def unique(array_of_items: List[T]) -> List[T]:
    temp_set: set[T] = set()
    idx: int = 0

    while idx < len(array_of_items):
        current_element: T = array_of_items[idx]
        temp_set.add(current_element)
        idx += 1

    temp_list: List[T] = []
    for current_element in temp_set:
        temp_list.append(current_element)

    sorted_list: List[T] = temp_list
    idx = 0
    while idx < len(sorted_list) - 1:
        jdx: int = idx + 1
        while jdx < len(sorted_list):
            if sorted_list[idx] > sorted_list[jdx]:
                temp_var: T = sorted_list[idx]
                sorted_list[idx] = sorted_list[jdx]
                sorted_list[jdx] = temp_var
            jdx += 1
        idx += 1

    return sorted_list