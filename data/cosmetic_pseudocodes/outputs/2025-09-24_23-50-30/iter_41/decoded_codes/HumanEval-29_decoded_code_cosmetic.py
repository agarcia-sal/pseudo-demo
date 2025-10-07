from typing import Iterable, List

def filter_by_prefix(collection: Iterable[str], key: str) -> List[str]:
    filtered: List[str] = []
    key_len = len(key)
    for element in collection:
        if element[:key_len] == key:
            filtered.append(element)
    return filtered