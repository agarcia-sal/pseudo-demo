from typing import Iterable, List, Any

def filter_integers(collection_of_items: Iterable[Any]) -> List[int]:
    result_container: List[int] = []
    idx: int = 0
    items = list(collection_of_items)  # Ensure indexable
    while idx < len(items):
        current_entry = items[idx]
        if not isinstance(current_entry, int):
            idx += 1
            continue
        result_container.append(current_entry)
        idx += 1
    return result_container