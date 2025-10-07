from typing import Sequence

def smallest_change(sequence: Sequence[int]) -> int:
    counter: int = 0
    position: int = 0
    half_length: int = (len(sequence) // 2)
    while position < half_length:
        left_val: int = sequence[position]
        right_val: int = sequence[len(sequence) - position - 1]
        if left_val != right_val:
            counter += 1
        position += 1
    return counter