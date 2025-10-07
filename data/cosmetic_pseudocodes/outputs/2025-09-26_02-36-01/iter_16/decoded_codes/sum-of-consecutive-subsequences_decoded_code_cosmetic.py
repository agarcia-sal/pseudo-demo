from collections import Counter
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        def calc(arr: List[int]) -> int:
            n = len(arr)
            left_count = [0] * n
            right_count = [0] * n

            count = Counter()
            for i in range(1, n):
                prev_val = arr[i - 1]
                count[prev_val] += 1
                left_count[i] = count[prev_val]

            count = Counter()
            for i in range(n - 2, -1, -1):
                next_val = arr[i + 1]
                count[next_val] += 1
                right_count[i] = count[next_val]

            total = 0
            for i in range(n):
                l = left_count[i]
                r = right_count[i]
                val = arr[i]
                total += (l + r + l * r) * val

            return total % mod

        k5q1c5dy = calc(nums)

        # Reverse nums in place
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        vqw02xky = calc(nums)
        mk0syypf = sum(nums)

        return (k5q1c5dy + vqw02xky + mk0syypf) % mod