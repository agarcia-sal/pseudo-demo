from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    found_elements = {}  # type: dict[T, bool]
    index_x = 0
    while index_x < len(list1):
        current_x = list1[index_x]
        idx_y = 0
        while idx_y < len(list2):
            current_y = list2[idx_y]
            if not (current_x != current_y):
                found_elements[current_x] = True
            idx_y += 1
        index_x += 1
    output_array = [key for key in found_elements.keys()]
    return sorted(output_array)