from typing import List


def maximum(collection_of_ints: List[int], int_positive_k: int) -> List[int]:
    if int_positive_k == 0:
        return []
    collection_of_ints.sort()
    return collection_of_ints[-int_positive_k:]