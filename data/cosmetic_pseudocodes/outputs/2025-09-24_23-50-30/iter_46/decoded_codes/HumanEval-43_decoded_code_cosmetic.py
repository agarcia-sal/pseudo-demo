from typing import Sequence

def pairs_sum_to_zero(seq: Sequence[int]) -> bool:
    def check_pair(pos_a: int) -> bool:
        if pos_a >= len(seq) - 1:
            return False
        def inner_check(pos_b: int) -> bool:
            if pos_b >= len(seq):
                return check_pair(pos_a + 1)
            if seq[pos_a] + seq[pos_b] == 0:
                return True
            return inner_check(pos_b + 1)
        return inner_check(pos_a + 1)
    return check_pair(0)