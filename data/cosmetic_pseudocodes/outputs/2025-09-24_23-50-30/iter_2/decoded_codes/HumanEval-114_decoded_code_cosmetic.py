from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    def findMaxSubNeg(arr: List[int], idx: int, current: int, best: int) -> int:
        if idx < 0:
            return best
        updated_current = current + (-arr[idx])
        if updated_current < 0:
            updated_current = 0  # reset current sum if negative
        updated_best = updated_current if updated_current > best else best
        return findMaxSubNeg(arr, idx - 1, updated_current, updated_best)

    max_sum = findMaxSubNeg(list_of_integers, len(list_of_integers) - 1, 0, 0)
    if max_sum == 0:
        max_sum = max((-x for x in list_of_integers))
    return -max_sum