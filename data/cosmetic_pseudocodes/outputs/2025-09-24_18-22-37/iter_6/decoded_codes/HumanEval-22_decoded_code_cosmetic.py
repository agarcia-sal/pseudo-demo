from typing import Iterable, List, Union

def filter_integers(sequence_of_items: Iterable[object]) -> List[int]:
    index_pointer: int = 0
    filtered_collection: List[int] = []
    sequence = list(sequence_of_items)  # Ensure indexing if input is not a sequence
    while index_pointer < len(sequence):
        current_item = sequence[index_pointer]
        if not isinstance(current_item, int):
            index_pointer += 1
            continue
        filtered_collection.append(current_item)
        index_pointer += 1
    return filtered_collection