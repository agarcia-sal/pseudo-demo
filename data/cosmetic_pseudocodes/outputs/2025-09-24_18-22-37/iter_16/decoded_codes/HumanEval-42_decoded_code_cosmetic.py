from typing import List, Sequence

def incr_list(sequence_of_items: Sequence[int]) -> List[int]:
    updated_collection: List[int] = []
    pos: int = 0
    while pos < len(sequence_of_items):
        current_value: int = sequence_of_items[pos]
        incremented_value: int = current_value + 1
        updated_collection.append(incremented_value)
        pos += 1
    return updated_collection