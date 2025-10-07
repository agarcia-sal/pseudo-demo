from typing import List

def incr_list(collection: List[int]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(collection):
        result.append(1 + collection[index])
        index += 1
    return result