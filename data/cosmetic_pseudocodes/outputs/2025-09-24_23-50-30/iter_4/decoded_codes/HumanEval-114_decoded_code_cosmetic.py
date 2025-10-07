from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    def negate(x: int) -> int:
        return -x

    def accumulate(arr: List[int], index: int, current_sum: int, best_sum: int) -> int:
        if index == len(arr):
            return best_sum
        updated_sum = max(0, current_sum + negate(arr[index]))
        updated_best = max(best_sum, updated_sum)
        return accumulate(arr, index + 1, updated_sum, updated_best)

    best_neg_sum = accumulate(list_of_integers, 0, 0, 0)
    minimum_sum = max(map(negate, list_of_integers)) if best_neg_sum == 0 else best_neg_sum
    return -minimum_sum