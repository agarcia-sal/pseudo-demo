from typing import List

def triples_sum_to_zero(arr_of_nums: List[int]) -> bool:
    def aux_i(i: int) -> bool:
        if i >= len(arr_of_nums) - 2:
            return False
        def aux_j(j: int) -> bool:
            if j >= len(arr_of_nums) - 1:
                return aux_i(i + 1)
            def aux_k(k: int) -> bool:
                if k >= len(arr_of_nums):
                    return aux_j(j + 1)
                if arr_of_nums[i] + arr_of_nums[j] + arr_of_nums[k] == 0:
                    return True
                return aux_k(k + 1)
            return aux_k(j + 1)
        return aux_j(i + 1)
    return aux_i(0)