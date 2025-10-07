from typing import Sequence, List, Any

def filter_integers(input_sequence: Sequence[Any]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    total_elements: int = len(input_sequence)

    while index_counter < total_elements:
        current_entry = input_sequence[index_counter]
        if isinstance(current_entry, int):
            result_collection.append(current_entry)
        index_counter += 1

    return result_collection