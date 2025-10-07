from typing import List, Sequence, TypeVar

T = TypeVar('T')

def maximum(data_set: Sequence[T], count_k: int) -> List[T]:
    if count_k != 0:
        sorted_data = sorted(data_set)
        boundary = len(sorted_data) - count_k
        result_collection: List[T] = []
        index_j = boundary
        while index_j < len(sorted_data):
            result_collection.append(sorted_data[index_j])
            index_j += 1
        return result_collection
    return []