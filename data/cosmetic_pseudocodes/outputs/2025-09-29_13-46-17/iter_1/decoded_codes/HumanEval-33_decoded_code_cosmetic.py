from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    list_copy: List[T] = list_input.copy()
    items_at_positions_divisible_by_three = sorted(
        list_copy[i] for i in range(0, len(list_copy), 3)
    )
    for idx, value in zip(range(0, len(list_copy), 3), items_at_positions_divisible_by_three):
        list_copy[idx] = value
    return list_copy