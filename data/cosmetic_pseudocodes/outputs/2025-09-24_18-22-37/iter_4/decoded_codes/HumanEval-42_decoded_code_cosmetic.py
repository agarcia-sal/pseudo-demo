from typing import Sequence, List

def incr_list(sequence: Sequence[int]) -> List[int]:
    result_sequence: List[int] = []
    index: int = 0
    while index < len(sequence):
        current_item: int = sequence[index]
        result_sequence.append(current_item + 1)
        index += 1
    return result_sequence