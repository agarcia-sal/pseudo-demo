from typing import List, TypeVar

T = TypeVar('T', bound=object)

def common(list1: List[T], list2: List[T]) -> List[T]:
    converged_elements = set()
    idx_outer = 0
    while idx_outer < len(list1):
        current_outer_element = list1[idx_outer]
        idx_inner = 0
        while idx_inner < len(list2):
            current_inner_element = list2[idx_inner]
            if current_outer_element == current_inner_element:
                converged_elements.add(current_outer_element)
                break
            idx_inner += 1
        idx_outer += 1
    ordered_result = sorted(converged_elements)
    return ordered_result