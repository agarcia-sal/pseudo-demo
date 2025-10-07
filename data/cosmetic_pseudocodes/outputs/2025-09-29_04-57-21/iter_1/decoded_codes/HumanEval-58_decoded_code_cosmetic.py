from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    found_elements = set()
    for index in range(len(list1)):
        current_item = list1[index]
        for candidate in list2:
            if candidate == current_item:
                found_elements.add(current_item)
    output_list = list(found_elements)
    output_list.sort()
    return output_list