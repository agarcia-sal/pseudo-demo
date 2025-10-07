from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_list: List[int] = []
    for element in list_of_values:
        if isinstance(element, int):
            result_list.append(element)
    return result_list