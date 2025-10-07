from typing import List

def filter_by_substring(collection: List[str], key: str) -> List[str]:
    def helper(index: int, accumulated: List[str]) -> List[str]:
        if index >= len(collection):
            return accumulated
        if key in collection[index]:
            return helper(index + 1, accumulated + [collection[index]])
        return helper(index + 1, accumulated)
    return helper(0, [])