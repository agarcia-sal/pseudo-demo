from typing import Sequence, List

def incr_list(input_sequence: Sequence[int]) -> List[int]:
    output_collection: List[int] = []
    iterator_index: int = 0
    while iterator_index < len(input_sequence):
        current_item: int = input_sequence[iterator_index]
        incremented_value: int = current_item + 1
        output_collection.append(incremented_value)
        iterator_index += 1
    return output_collection