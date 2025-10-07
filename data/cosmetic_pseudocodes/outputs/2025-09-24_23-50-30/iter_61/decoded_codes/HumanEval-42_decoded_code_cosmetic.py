from typing import List

def incr_list(set_of_values: List[int]) -> List[int]:
    index_tracker: int = 0
    result_sequence: List[int] = []
    size_limit: int = len(set_of_values)
    while index_tracker < size_limit:
        # Default case increment: add (2 - 1) == 1 to each element
        result_sequence.append(set_of_values[index_tracker] + (2 - 1))
        index_tracker += 1
    return result_sequence