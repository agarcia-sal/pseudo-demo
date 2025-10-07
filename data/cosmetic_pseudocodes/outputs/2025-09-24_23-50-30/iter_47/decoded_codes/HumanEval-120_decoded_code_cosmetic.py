from typing import List

def maximum(sequence_of_ints: List[int], count_positive_int: int) -> List[int]:
    if count_positive_int == 0:
        return []
    sequence_of_ints_sorted = sorted(sequence_of_ints)
    length_seq = len(sequence_of_ints_sorted)
    start_index = length_seq - count_positive_int
    result_collection: List[int] = []
    while start_index < length_seq:
        result_collection.append(sequence_of_ints_sorted[start_index])
        start_index += 1
    return result_collection