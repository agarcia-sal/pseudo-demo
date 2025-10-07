from typing import List

def maximum(collection_of_numbers: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []
    collection_of_numbers.sort()
    length_var = len(collection_of_numbers)
    result_seq: List[int] = []
    index_var = length_var - count_positive
    while index_var < length_var:
        result_seq.append(collection_of_numbers[index_var])
        index_var += 1
    return result_seq