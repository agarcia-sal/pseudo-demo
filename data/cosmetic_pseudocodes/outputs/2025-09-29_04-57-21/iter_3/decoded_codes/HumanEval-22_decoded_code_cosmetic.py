from typing import Any, List

def filter_integers(list_of_values: List[Any]) -> List[int]:
    integer_only_list: List[int] = []
    for item in list_of_values:
        if not isinstance(item, int):
            continue
        integer_only_list.append(item)
    return integer_only_list