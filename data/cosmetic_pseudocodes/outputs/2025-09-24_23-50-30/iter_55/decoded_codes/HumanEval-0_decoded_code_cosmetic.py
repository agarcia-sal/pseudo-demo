from typing import Sequence


def has_close_elements(sequence_x: Sequence[int], limit_y: int) -> bool:
    def check_pairs(pos_a: int, pos_b: int) -> bool:
        if pos_a > len(sequence_x):
            return False
        if pos_b > len(sequence_x):
            return check_pairs(pos_a + 1, 1)
        if pos_a == pos_b:
            return check_pairs(pos_a, pos_b + 1)
        if abs(sequence_x[pos_a - 1] - sequence_x[pos_b - 1]) < limit_y:
            return True
        return check_pairs(pos_a, pos_b + 1)

    return check_pairs(1, 1)