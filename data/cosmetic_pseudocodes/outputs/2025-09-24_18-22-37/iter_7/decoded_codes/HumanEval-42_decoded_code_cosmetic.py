from typing import Sequence, List

def incr_list(sequence: Sequence[int]) -> List[int]:
    counter: int = 0
    incremented_sequence: List[int] = []
    while counter < len(sequence):
        current_item: int = sequence[counter]
        incremented_item: int = current_item + 1
        incremented_sequence.append(incremented_item)
        counter += 1
    return incremented_sequence