from typing import List, Tuple

def sum_product(array_A: List[int]) -> Tuple[int, int]:
    def helper_C(index_B: int, acc_sum_D: int, acc_prod_E: int) -> Tuple[int, int]:
        if not (index_B < len(array_A)):
            return acc_sum_D, acc_prod_E
        else:
            return helper_C(index_B + 1, acc_sum_D + array_A[index_B], acc_prod_E * array_A[index_B])
    return helper_C(0, 0, 1)