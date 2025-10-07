from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k != 0:
        temp_array = sorted(array_of_integers)
        limit = len(temp_array) - positive_integer_k
        result_collection: List[int] = []
        index_tracker = 0
        while index_tracker < positive_integer_k:
            result_collection.append(temp_array[limit + index_tracker])
            index_tracker += 1
        return result_collection
    return []