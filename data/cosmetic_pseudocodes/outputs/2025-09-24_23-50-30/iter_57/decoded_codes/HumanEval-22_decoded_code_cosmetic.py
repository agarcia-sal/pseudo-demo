from typing import Any, List

def filter_integers(array_of_any: List[Any]) -> List[int]:
    result_collection: List[int] = []
    idx: int = 0
    while idx < len(array_of_any):
        current_candidate = array_of_any[idx]
        if not (not isinstance(current_candidate, int)):
            result_collection.append(current_candidate)
        idx += 1
    return result_collection