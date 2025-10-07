from typing import Iterable, List, Union

def filter_integers(sequence_of_items: Iterable[object]) -> List[int]:
    refined_collection: List[int] = []
    iterator_index: int = 0
    items_list = list(sequence_of_items)  # to support indexing

    while iterator_index < len(items_list):
        current_candidate = items_list[iterator_index]
        if isinstance(current_candidate, int):
            refined_collection.append(current_candidate)
        iterator_index += 1

    return refined_collection