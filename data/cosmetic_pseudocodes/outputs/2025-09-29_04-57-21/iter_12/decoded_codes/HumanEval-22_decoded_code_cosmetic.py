from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    n: int = len(list_of_values)

    while index_counter < n:
        candidate = list_of_values[index_counter]
        if isinstance(candidate, int):
            result_collection.append(candidate)
        index_counter += 1

    return result_collection