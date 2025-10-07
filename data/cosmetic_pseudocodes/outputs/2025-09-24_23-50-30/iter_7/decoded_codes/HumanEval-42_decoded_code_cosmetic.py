from typing import List

def incr_list(collection: List[int]) -> List[int]:
    result_collection: List[int] = []
    index: int = 0
    while index < len(collection):
        result_collection.append(collection[index] + 1)
        index += 1
    return result_collection