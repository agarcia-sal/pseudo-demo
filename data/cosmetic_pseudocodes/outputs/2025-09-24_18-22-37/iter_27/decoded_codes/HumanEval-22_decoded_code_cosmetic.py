from typing import Iterable, List, Any

def filter_integers(sequence_of_items: Iterable[Any]) -> List[int]:
    filtered_results: List[int] = []
    idx_counter: int = 0
    sequence_as_list = list(sequence_of_items)
    total_elements: int = len(sequence_as_list)
    while idx_counter < total_elements:
        candidate = sequence_as_list[idx_counter]
        if isinstance(candidate, int):
            filtered_results.append(candidate)
        idx_counter += 1
    return filtered_results