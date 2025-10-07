from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    result_set: set[T] = set()
    for element_index in range(len(list_of_elements)):
        current_item = list_of_elements[element_index]
        result_set.add(current_item)

    intermediate_list: List[T] = []
    for item in result_set:
        intermediate_list.append(item)

    final_sorted_list: List[T] = sorted(intermediate_list)
    return final_sorted_list