from typing import Iterable, List

def get_positive(collection: Iterable[int]) -> List[int]:
    result: List[int] = []
    for item in collection:
        if item > 0:
            result.append(item)
    return result