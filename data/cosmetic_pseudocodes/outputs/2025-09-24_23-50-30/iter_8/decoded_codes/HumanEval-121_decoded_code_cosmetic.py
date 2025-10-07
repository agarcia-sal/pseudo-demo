from typing import Sequence

def solution(input_sequence: Sequence[int]) -> int:
    accumulator = 0
    position = 0
    length = len(input_sequence)
    while position < length:
        element = input_sequence[position]
        # position is even if position % 2 == 0 (so position % 2 != 1)
        # element is odd if element % 2 != 0
        if (position % 2 != 1) and (element % 2 != 0):
            accumulator += element
        position += 1
    return accumulator