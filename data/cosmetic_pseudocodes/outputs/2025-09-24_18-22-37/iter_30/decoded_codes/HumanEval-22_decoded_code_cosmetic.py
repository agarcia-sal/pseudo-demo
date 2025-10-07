from typing import Iterable, List, Union

def filter_integers(sequence_of_items: Iterable[object]) -> List[int]:
    filtered_collection: List[int] = []
    position: int = 0
    sequence_list = list(sequence_of_items)  # Ensure indexing support
    while position < len(sequence_list):
        candidate = sequence_list[position]
        if isinstance(candidate, int):
            filtered_collection.append(candidate)
        position += 1
    return filtered_collection