from typing import List

def minSubArraySum(collection_of_ints: List[int]) -> int:
    acc_sum: int = 0
    max_sum: int = 0
    for idx in range(len(collection_of_ints)):
        val = 0 - collection_of_ints[idx]
        acc_sum = max(acc_sum + val, 0)
        max_sum = max(max_sum, acc_sum)
    if max_sum == 0:
        max_sum = max(0 - x for x in collection_of_ints)
    result: int = 0 - max_sum
    return result