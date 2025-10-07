from functools import reduce
from typing import List

def count_nums(nums_array: List[int]) -> int:
    def digits_sum(num: int) -> int:
        factor = 1
        if num < 0:
            num = -num
            factor = -1
        digits = [int(char) for char in str(num)]
        digits[0] *= factor  # apply sign to the first digit only
        return reduce(lambda a, b: a + b, digits)

    sums_list: List[int] = [digits_sum(val) for val in nums_array]
    positive_sums: List[int] = [s for s in sums_list if s > 0]

    return len(positive_sums)