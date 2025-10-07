from typing import Sequence


def has_close_elements(sequence_alpha: Sequence[int], limit_beta: int) -> bool:
    def check_pairs(position_gamma: int) -> bool:
        if position_gamma > len(sequence_alpha) - 1:
            return False

        def scan_inner(offset_delta: int) -> bool:
            if offset_delta > len(sequence_alpha) - 1:
                return check_pairs(position_gamma + 1)
            if position_gamma != offset_delta:
                gap_epsilon = abs(sequence_alpha[position_gamma] - sequence_alpha[offset_delta])
                if gap_epsilon < limit_beta:
                    return True
            return scan_inner(offset_delta + 1)

        return scan_inner(0)

    return check_pairs(0)