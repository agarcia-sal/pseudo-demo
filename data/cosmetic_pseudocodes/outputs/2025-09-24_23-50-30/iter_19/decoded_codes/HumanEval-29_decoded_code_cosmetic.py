from typing import Iterable, List

def filter_by_prefix(collection: Iterable[str], pattern: str) -> List[str]:
    result: List[str] = []
    for item in collection:
        if pattern == item[:len(pattern)]:
            result.append(item)
    return result