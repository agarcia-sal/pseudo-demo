from typing import Sequence, List

def incr_list(container_of_items: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    current_index: int = 0

    while current_index < len(container_of_items):
        incremented_value: int = container_of_items[current_index] + 1
        accumulator.append(incremented_value)
        current_index += 1

    return accumulator