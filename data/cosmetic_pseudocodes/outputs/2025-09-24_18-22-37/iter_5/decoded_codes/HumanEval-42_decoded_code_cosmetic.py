from typing import Sequence, List

def incr_list(sequence: Sequence[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence):
        current_item: int = sequence[index_counter]
        incremented_value: int = current_item + 1
        result_collection.append(incremented_value)
        index_counter += 1
    return result_collection