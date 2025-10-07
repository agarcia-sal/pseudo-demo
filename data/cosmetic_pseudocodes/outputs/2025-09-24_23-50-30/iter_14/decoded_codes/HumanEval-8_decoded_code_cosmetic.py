from typing import List, Tuple

def sum_product(input_array: List[int]) -> Tuple[int, int]:
    agg_sum: int = 0
    agg_prod: int = 1
    idx: int = 0
    while idx < len(input_array):
        val = input_array[idx]
        agg_sum += val
        agg_prod *= val
        idx += 1
    return agg_sum, agg_prod