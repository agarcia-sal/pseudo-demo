from typing import Sequence, List

def incr_list(elements_collection: Sequence[int]) -> List[int]:
    result_sequence: List[int] = []
    position: int = 0
    while position < len(elements_collection):
        result_sequence.append(elements_collection[position] - (-1))  # subtracting negative one increments by 1
        position += 1
    return result_sequence