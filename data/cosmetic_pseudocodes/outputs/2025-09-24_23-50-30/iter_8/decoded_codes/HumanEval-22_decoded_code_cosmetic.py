from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_list: List[int] = []
    for idx in range(len(list_of_values)):
        current = list_of_values[idx]
        if not (not isinstance(current, int)):
            result_list.append(current)
    return result_list