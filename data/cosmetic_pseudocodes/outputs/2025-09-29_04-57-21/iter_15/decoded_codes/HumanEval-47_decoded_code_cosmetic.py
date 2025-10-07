from typing import Sequence, Union, TypeVar

T = TypeVar('T', bound=Union[int, float])

def median(list_of_elements: Sequence[T]) -> float:
    sorted_items = sorted(list_of_elements)
    total_count = len(sorted_items)
    if total_count % 2 == 0:
        mid_pos = total_count // 2
        left_val = sorted_items[mid_pos - 1]
        right_val = sorted_items[mid_pos]
        return (left_val + right_val) * 0.5
    return float(sorted_items[(total_count - 1) // 2])