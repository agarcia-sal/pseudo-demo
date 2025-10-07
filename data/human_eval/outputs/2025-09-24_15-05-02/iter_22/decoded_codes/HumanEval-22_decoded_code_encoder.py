from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    list_of_integers: List[int] = []
    for value in list_of_values:
        if isinstance(value, int):
            list_of_integers.append(value)
    return list_of_integers