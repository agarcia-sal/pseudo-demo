from typing import Iterable, List, Union

def filter_integers(sequence_of_entries: Iterable[object]) -> List[int]:
    filtered_collection: List[int] = []
    iterator_index: int = 0
    entries_list = list(sequence_of_entries)  # Ensure indexing is supported
    while iterator_index < len(entries_list):
        current_candidate = entries_list[iterator_index]
        if isinstance(current_candidate, int):
            filtered_collection.append(current_candidate)
        iterator_index += 1
    return filtered_collection