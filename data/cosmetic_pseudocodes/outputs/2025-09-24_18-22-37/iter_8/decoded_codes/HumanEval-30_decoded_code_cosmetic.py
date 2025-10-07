from typing import Sequence, List


def get_positive(sequence_elements: Sequence[int]) -> List[int]:
    collected_items: List[int] = []
    current_index: int = 0
    while current_index < len(sequence_elements):
        inspected_item: int = sequence_elements[current_index]
        if inspected_item > 0:
            collected_items.append(inspected_item)
        current_index += 1
    return collected_items