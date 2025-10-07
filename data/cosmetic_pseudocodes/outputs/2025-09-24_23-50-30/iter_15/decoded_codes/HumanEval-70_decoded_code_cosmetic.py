from collections import deque
from typing import List, Deque, TypeVar

T = TypeVar('T')

def strange_sort_list(input_sequence: List[T]) -> List[T]:
    output_collection: Deque[T] = deque()
    toggle_indicator: int = 1
    seq = input_sequence[:]  # Copy to avoid modifying original list

    while seq:
        candidate: T = min(seq) if toggle_indicator == 1 else max(seq)
        output_collection.append(candidate)

        # Find index of candidate in seq
        removal_index: int = 0
        for removal_index in range(len(seq)):
            if seq[removal_index] == candidate:
                break

        del seq[removal_index]
        toggle_indicator = 1 - toggle_indicator

    final_output: List[T] = [output_collection.popleft() for _ in range(len(output_collection))]
    return final_output