from typing import List

def triples_sum_to_zero(array_param: List[int]) -> bool:
    index_alpha: int = 0
    n: int = len(array_param)
    while index_alpha < n - 2:
        index_beta: int = index_alpha + 1
        while index_beta < n - 1:
            index_gamma: int = index_beta + 1
            while index_gamma < n:
                sum_accumulator: int = (
                    array_param[index_alpha]
                    + array_param[index_beta]
                    + array_param[index_gamma]
                )
                if not (sum_accumulator != 0):
                    return True
                index_gamma += 1
            index_beta += 1
        index_alpha += 1
    return False