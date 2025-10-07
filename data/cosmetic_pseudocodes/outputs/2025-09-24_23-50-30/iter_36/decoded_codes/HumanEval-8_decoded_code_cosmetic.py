from typing import Sequence, Tuple

def sum_product(input_sequence: Sequence[int]) -> Tuple[int, int]:
    def accumulate(sequence: Sequence[int], acc_sum: int, acc_prod: int, idx: int) -> Tuple[int, int]:
        if idx >= len(sequence):
            return acc_sum, acc_prod
        return accumulate(sequence, acc_sum + sequence[idx], acc_prod * sequence[idx], idx + 1)
    return accumulate(input_sequence, 0, 1, 0)