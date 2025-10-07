from typing import Any, List

def filter_integers(values: List[Any]) -> List[int]:
    integer_list: List[int] = []
    for item in values:
        if isinstance(item, int):
            integer_list.append(item)
    return integer_list