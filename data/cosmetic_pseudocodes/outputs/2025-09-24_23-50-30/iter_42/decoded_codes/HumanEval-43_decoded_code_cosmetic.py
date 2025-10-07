from typing import List


def pairs_sum_to_zero(array_of_nums: List[int]) -> bool:
    indexer_outer: int = 0
    while indexer_outer < len(array_of_nums):
        indexer_inner: int = indexer_outer + 1
        while indexer_inner < len(array_of_nums):
            sum_candidate: int = array_of_nums[indexer_inner] + array_of_nums[indexer_outer]
            if sum_candidate == 0:
                return True
            indexer_inner += 1
        indexer_outer += 1
    return False