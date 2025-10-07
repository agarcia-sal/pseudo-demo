from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_collection = sorted(array_of_integers)
    start_index = len(sorted_collection) - positive_integer_k
    return sorted_collection[start_index:]