from typing import Sequence, List

def get_positive(input_sequence: Sequence[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(input_sequence):
        current_entry: int = input_sequence[index_counter]
        if current_entry > 0:
            result_collection.append(current_entry)
        index_counter += 1
    return result_collection