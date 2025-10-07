from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    result_list: List[int] = []
    index_tracker: int = 0
    while index_tracker < len(list_of_values):
        current_item = list_of_values[index_tracker]
        if not isinstance(current_item, int):
            index_tracker += 1
            continue
        result_list.append(current_item)
        index_tracker += 1
    return result_list