from typing import List

def sort_array(nums: List[int]) -> List[int]:
    def helper(x: int) -> int:
        return bin(x).count('1')

    nums_sorted = list(nums)
    nums_sorted.sort()

    n = len(nums_sorted)
    for i in range(1, n):
        for j in range(n - i):
            hj = helper(nums_sorted[j])
            hj1 = helper(nums_sorted[j + 1])
            if hj > hj1 or (hj == hj1 and nums_sorted[j] > nums_sorted[j + 1]):
                nums_sorted[j], nums_sorted[j + 1] = nums_sorted[j + 1], nums_sorted[j]

    return nums_sorted