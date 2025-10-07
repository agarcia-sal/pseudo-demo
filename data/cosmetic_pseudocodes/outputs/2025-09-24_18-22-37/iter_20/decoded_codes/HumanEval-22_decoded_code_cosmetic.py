from typing import Iterable, List, Any

def filter_integers(collection_of_items: Iterable[Any]) -> List[int]:
    result_container: List[int] = []
    idx: int = 0
    collection_list = list(collection_of_items)  # to support index access and length reliably
    total_count: int = len(collection_list)
    while idx < total_count:
        current_item = collection_list[idx]
        type_check = type(current_item)
        if type_check is not int:
            idx += 1
            continue
        result_container.append(current_item)
        idx += 1
    return result_container