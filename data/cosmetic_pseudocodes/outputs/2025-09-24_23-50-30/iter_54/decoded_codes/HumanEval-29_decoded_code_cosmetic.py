from typing import List

def filter_by_prefix(collection: List[str], target: str) -> List[str]:
    result: List[str] = []
    index: int = 0
    while index < len(collection):
        if collection[index][:len(target)] == target:
            result.append(collection[index])
        index += 1
    return result