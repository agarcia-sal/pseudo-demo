from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(input_array: List[T]) -> Optional[T]:
    deduplicated_values = list(set(input_array))
    ascending_order_values = sorted(deduplicated_values)
    if len(ascending_order_values) <= 1:
        return None
    second_minimum = ascending_order_values[1]
    return second_minimum