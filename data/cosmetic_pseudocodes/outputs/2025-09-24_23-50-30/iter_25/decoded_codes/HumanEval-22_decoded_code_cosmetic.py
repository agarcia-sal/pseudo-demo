from typing import Iterable, List, Any

def filter_integers(sequence_of_items: Iterable[Any]) -> List[int]:
    filtered_collection: List[int] = []
    for candidate_element in sequence_of_items:
        if not isinstance(candidate_element, int):
            continue
        filtered_collection.append(candidate_element)
    return filtered_collection