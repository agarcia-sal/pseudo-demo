from typing import List, Tuple

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_prefix_sum: int = 0
    curr_sum: int = 0

    def maxNegPrefix(arr: List[int]) -> int:
        if not arr:
            return float('-inf')
        first_neg = -arr[0]
        rest_max = maxNegPrefix(arr[1:])
        return first_neg if first_neg > rest_max else rest_max

    max_neg_prefix = maxNegPrefix(list_of_integers)

    def helper(sublist: List[int]) -> Tuple[int, int]:
        nonlocal max_prefix_sum, curr_sum
        if not sublist:
            return max_prefix_sum, curr_sum
        neg_val = -sublist[0]
        curr_sum_new = curr_sum + neg_val
        curr_sum = 0 if curr_sum_new < 0 else curr_sum_new
        max_prefix_sum = curr_sum if curr_sum > max_prefix_sum else max_prefix_sum
        return helper(sublist[1:])

    max_prefix_sum_final, curr_sum_final = helper(list_of_integers)

    max_prefix_sum = max_prefix_sum_final
    curr_sum = curr_sum_final

    if max_prefix_sum == 0:
        max_prefix_sum = max_neg_prefix

    return -max_prefix_sum