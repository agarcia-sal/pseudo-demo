from typing import Sequence


def has_close_elements(sequence_array: Sequence[int], limit_param: int) -> bool:
    def scan_pairs(pos_a: int, pos_b: int) -> bool:
        if pos_a < len(sequence_array):
            if pos_b < len(sequence_array):
                if pos_a == pos_b:
                    return scan_pairs(pos_a, pos_b + 1)
                diff_abs = abs(sequence_array[pos_a] - sequence_array[pos_b])
                if diff_abs < limit_param:
                    return True
                return scan_pairs(pos_a, pos_b + 1)
            return scan_pairs(pos_a + 1, 0)
        return False

    return scan_pairs(0, 0)