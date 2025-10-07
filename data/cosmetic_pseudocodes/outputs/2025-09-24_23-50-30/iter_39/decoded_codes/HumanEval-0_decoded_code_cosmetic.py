from typing import Sequence

def has_close_elements(seq_A: Sequence[float], val_Z: float) -> bool:
    def aux_func(pos_M: int, pos_N: int) -> bool:
        if pos_M >= len(seq_A):
            return False
        elif pos_N >= len(seq_A):
            return aux_func(pos_M + 1, 0)
        else:
            result_B = (pos_M != pos_N) and (abs(seq_A[pos_M] - seq_A[pos_N]) < val_Z)
            return True if result_B else aux_func(pos_M, pos_N + 1)
    return aux_func(0, 0)