from typing import Iterable, Tuple

def sum_product(collection_of_numbers: Iterable[int]) -> Tuple[int, int]:
    nums = list(collection_of_numbers)
    def aux(index: int, agg_sum: int, agg_product: int) -> Tuple[int, int]:
        if index >= len(nums):
            return agg_sum, agg_product
        return aux(index + 1, agg_sum + nums[index], agg_product * nums[index])
    return aux(0, 0, 1)