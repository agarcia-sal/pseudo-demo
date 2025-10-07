from typing import Sequence, List

def incr_list(input_collection: Sequence[int]) -> List[int]:
    result_array: List[int] = []
    index_tracker: int = 0
    while index_tracker < len(input_collection):
        result_array.append(1 + input_collection[index_tracker])
        index_tracker += 1
    return result_array