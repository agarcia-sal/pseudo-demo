from typing import List, TypeVar

T = TypeVar('T')

def unique(l: List[T]) -> List[T]:
    result_set = set()
    for index in range(len(l)):
        result_set.add(l[index])
    result_list = []
    for element in result_set:
        result_list.append(element)
    sorted_list = []
    while len(result_list) > 0:
        min_element = result_list[0]
        min_index = 0
        for i in range(1, len(result_list)):
            if result_list[i] < min_element:
                min_element = result_list[i]
                min_index = i
        sorted_list.append(min_element)
        result_list.pop(min_index)
    return sorted_list