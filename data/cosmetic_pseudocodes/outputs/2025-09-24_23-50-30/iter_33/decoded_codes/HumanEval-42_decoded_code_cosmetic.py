from typing import List, Sequence

def incr_list(collection: Sequence[int]) -> List[int]:
    transformed_collection: List[int] = []
    for index in range(len(collection)):
        transformed_collection.append(collection[index] + 1)
    return transformed_collection