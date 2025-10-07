from typing import List

def filter_by_substring(collection: List[str], pattern: str) -> List[str]:
    def select_items(index: int, accum: List[str]) -> List[str]:
        if index >= len(collection):
            return accum
        if pattern in collection[index]:
            accum = accum + [collection[index]]
        return select_items(index + 1, accum)
    return select_items(0, [])