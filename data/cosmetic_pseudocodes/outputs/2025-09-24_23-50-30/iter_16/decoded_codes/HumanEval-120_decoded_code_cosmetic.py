from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if not (positive_integer_k > 0):
        return []

    sorted_collection: List[int] = []
    for item in array_of_integers:
        # Insert item into sorted_collection to maintain non-decreasing order
        # Using binary search for efficient insertion
        from bisect import insort
        insort(sorted_collection, item)

    start_index = len(sorted_collection) - positive_integer_k
    if start_index < 0:
        start_index = 0

    result_sequence: List[int] = []
    current_index = start_index

    while current_index < len(sorted_collection):
        result_sequence.append(sorted_collection[current_index])
        current_index += 1

    return result_sequence