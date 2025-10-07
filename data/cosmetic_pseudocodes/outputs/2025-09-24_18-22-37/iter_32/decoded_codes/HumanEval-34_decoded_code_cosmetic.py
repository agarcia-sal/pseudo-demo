from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = set()
    for index in range(len(list_of_elements)):
        temp_set.add(list_of_elements[index])

    temp_list = []
    for element in temp_set:
        temp_list.append(element)

    sorted_list = sorted(temp_list)

    return sorted_list