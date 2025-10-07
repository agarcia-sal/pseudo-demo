from typing import List

def maximum(numbers_collection: List[int], limit_positive: int) -> List[int]:
    if limit_positive == 0:
        return []
    sorted_collection = sorted(numbers_collection)
    collection_length = len(sorted_collection)
    start_index = collection_length - limit_positive
    return sorted_collection[start_index:collection_length]