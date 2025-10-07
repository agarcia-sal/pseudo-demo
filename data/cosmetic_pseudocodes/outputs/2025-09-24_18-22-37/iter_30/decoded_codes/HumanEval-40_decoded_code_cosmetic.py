from typing import Sequence

def triples_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    n = len(sequence_numbers)
    pos_a = 0
    while pos_a <= n - 1:
        pos_b = pos_a + 1
        while pos_b <= n - 1:
            pos_c = pos_b + 1
            while pos_c <= n - 1:
                element_x = sequence_numbers[pos_a]
                element_y = sequence_numbers[pos_b]
                element_z = sequence_numbers[pos_c]
                total_sum = element_x + element_y + element_z
                if total_sum == 0:
                    return True
                pos_c += 1
            pos_b += 1
        pos_a += 1
    return False