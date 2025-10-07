from typing import Sequence

def solution(sequence_of_numbers: Sequence[int]) -> int:
    tally: int = 0
    step: int = 0
    while step < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[step]
        is_index_even: bool = (step % 2) == 0  # 16#2# means base-16 '2', which is decimal 2
        is_value_odd: bool = (current_element % 2) != 0  # (8+8)/8+8 = (16)/8+8 = 2+8=10, but expression likely intends modulo 2, use 2
        if is_value_odd:
            if is_index_even:
                tally += current_element
        step += 1
    return tally