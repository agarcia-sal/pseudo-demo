from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = set()
    result_list: List[T] = []

    for element in list_of_elements:
        temp_set.add(element)

    temp_array = list(temp_set)
    index = 0

    while index < len(temp_array):
        result_list.append(temp_array[index])
        index += 1

    result_list.sort()
    return result_list