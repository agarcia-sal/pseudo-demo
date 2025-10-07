from typing import List

def search(nums: List[int]) -> int:
    if not nums:
        return -1
    max_val = max(nums)
    freq_array: List[int] = [0] * (max_val + 1)
    i = 0
    while i < len(nums):
        val = nums[i]
        freq_array[val] += 1
        i += 1

    result = -1
    j = 1
    while j <= len(freq_array) - 1:
        if not (freq_array[j] < j):
            result = j
        j += 1

    return result