from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_list: List[int] = []
    for index in range(len(list_of_values)):
        current_item = list_of_values[index]
        if isinstance(current_item, int):
            result_list.append(current_item)
    return result_list