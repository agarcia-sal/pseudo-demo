from typing import Iterable, List, Any

def filter_integers(values_collection: Iterable[Any]) -> List[int]:
    result: List[int] = []
    for item in values_collection:
        if not isinstance(item, int):
            continue
        result.append(item)
    return result