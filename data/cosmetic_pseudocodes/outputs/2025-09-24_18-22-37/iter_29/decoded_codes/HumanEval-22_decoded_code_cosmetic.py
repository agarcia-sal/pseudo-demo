from typing import Any, List, Sequence

def filter_integers(container_of_items: Sequence[Any]) -> List[int]:
    result_list: List[int] = []
    position: int = 0
    length: int = len(container_of_items)
    while position < length:
        current_item = container_of_items[position]
        if isinstance(current_item, int):
            result_list.append(current_item)
        position += 1
    return result_list