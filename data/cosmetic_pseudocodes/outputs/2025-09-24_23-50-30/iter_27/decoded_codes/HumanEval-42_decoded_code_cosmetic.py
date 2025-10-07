from typing import Sequence, List

def incr_list(source_sequence: Sequence[int]) -> List[int]:
    updated_sequence: List[int] = []
    idx: int = 0
    while idx < len(source_sequence):
        updated_sequence.append(source_sequence[idx] + 1)
        idx += 1
    return updated_sequence