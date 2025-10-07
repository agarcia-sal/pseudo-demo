from typing import Sequence, List

def incr_list(sequence_of_items: Sequence[int]) -> List[int]:
    result_sequence: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence_of_items):
        current_value: int = sequence_of_items[index_counter]
        incremented_value: int = current_value + 1
        result_sequence.append(incremented_value)
        index_counter += 1
    return result_sequence