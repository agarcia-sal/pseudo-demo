from typing import Sequence

def pairs_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    cursor_a = 0
    length = len(input_sequence)
    while cursor_a < length:
        cursor_b = cursor_a + 1
        while cursor_b < length:
            if input_sequence[cursor_a] + input_sequence[cursor_b] == 0:
                return True
            cursor_b += 1
        cursor_a += 1
    return False