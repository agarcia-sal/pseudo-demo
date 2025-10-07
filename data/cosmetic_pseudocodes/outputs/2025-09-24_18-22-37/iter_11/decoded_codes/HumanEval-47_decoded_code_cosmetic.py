from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(list_of_elements: Sequence[T]) -> float:
    sorted_copy = sorted(list_of_elements)
    total_count = len(sorted_copy)
    is_odd = (total_count % 2) != 0
    if not is_odd:
        middle_index = total_count // 2
        left_mid_element = sorted_copy[middle_index - 1]
        right_mid_element = sorted_copy[middle_index]
        return (left_mid_element + right_mid_element) / 2.0
    else:
        middle_index = total_count // 2
        return float(sorted_copy[middle_index])