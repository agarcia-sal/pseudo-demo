from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k != 0:
        sorted_nums = sorted(array_of_integers)
        idx = len(sorted_nums) - positive_integer_k
        return [sorted_nums[i] for i in range(idx, len(sorted_nums))]
    else:
        return []