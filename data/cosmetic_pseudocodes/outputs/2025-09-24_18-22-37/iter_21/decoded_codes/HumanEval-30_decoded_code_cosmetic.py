from typing import List, Sequence

def get_positive(collection_of_values: Sequence[int]) -> List[int]:
    result: List[int] = []
    idx: int = 1
    while idx <= len(collection_of_values):
        if collection_of_values[idx - 1] > 0:
            result.append(collection_of_values[idx - 1])
        idx += 1
    return result