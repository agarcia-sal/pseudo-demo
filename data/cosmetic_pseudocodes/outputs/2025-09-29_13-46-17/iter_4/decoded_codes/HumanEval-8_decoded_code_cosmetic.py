from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def recursive_helper(sequence: List[int], index: int, acc_sum: int, acc_prod: int) -> Tuple[int, int]:
        if index >= len(sequence):
            return acc_sum, acc_prod
        current_val = sequence[index]
        return recursive_helper(sequence, index + 1, acc_sum + current_val, acc_prod * current_val)

    return recursive_helper(list_of_integers, 0, 0, 1)