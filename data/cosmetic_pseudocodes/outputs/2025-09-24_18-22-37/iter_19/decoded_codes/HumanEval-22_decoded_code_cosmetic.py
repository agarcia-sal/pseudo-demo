from typing import Sequence, List, Any


def filter_integers(sequence: Sequence[Any]) -> List[int]:
    filtered_results: List[int] = []
    idx: int = 0
    while idx < len(sequence):
        current_element = sequence[idx]
        if isinstance(current_element, int):
            filtered_results.append(current_element)
        idx += 1
    return filtered_results