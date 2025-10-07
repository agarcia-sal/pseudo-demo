from typing import List, TypeVar

T = TypeVar('T')

def maximum(input_array: List[T], count: int) -> List[T]:
    if count <= 0:
        return []
    sorted_collection: List[T] = []
    for val in input_array:
        inserted = False
        for j in range(len(sorted_collection)):
            if val < sorted_collection[j]:
                sorted_collection.insert(j, val)
                inserted = True
                break
        if not inserted:
            sorted_collection.append(val)
    return sorted_collection[-count:]