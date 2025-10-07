from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    position_a = 0
    while position_a <= length - 1:
        idx_b = position_a + 1
        while idx_b <= length - 1:
            cursor_c = idx_b + 1
            while cursor_c <= length - 1:
                value_x = sequence_of_numbers[position_a]
                value_y = sequence_of_numbers[idx_b]
                value_z = sequence_of_numbers[cursor_c]
                sum_total = value_x + value_y + value_z
                if sum_total == 0:
                    return True
                else:
                    cursor_c += 1
            idx_b += 1
        position_a += 1
    return False