from typing import Sequence


def triples_sum_to_zero(sequence_p: Sequence[int]) -> bool:
    length = len(sequence_p)
    pos_x = 0
    while pos_x <= length - 1:
        pos_y = pos_x + 1
        while pos_y <= length - 1:
            pos_z = pos_y + 1
            while pos_z <= length - 1:
                val_a = sequence_p[pos_x]
                val_b = sequence_p[pos_y]
                val_c = sequence_p[pos_z]
                total_sum = val_a + val_b + val_c
                if total_sum == 0:
                    return True
                pos_z += 1
            pos_y += 1
        pos_x += 1
    return False