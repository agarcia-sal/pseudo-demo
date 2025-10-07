from collections import defaultdict
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        alpha = 0
        n = len(nums)
        # Find maximum value in nums
        for k in range(n):
            if nums[k] > alpha:
                alpha = nums[k]

        omega = defaultdict(int)
        # Count frequency of each number
        for idx in range(n):
            omega[nums[idx]] += 1

        tau = [0] * (alpha + 1)

        r1 = alpha
        while r1 >= 1:
            c1 = 0
            r2 = r1
            while r2 <= alpha:
                c1 += omega[r2] if r2 in omega else 0
                tau[r1] -= tau[r2]
                r2 += r1
            tau[r1] += c1 * (c1 - 1) // 2
            r1 -= 1

        acc = [0] * (alpha + 1)
        scnt = 0
        for i in range(1, alpha + 1):
            scnt += tau[i]
            acc[i] = scnt

        output = []
        for elem in queries:
            left = 1
            right = alpha
            pos = right + 1
            while left <= right:
                mid = (left + right) // 2
                if acc[mid] > elem:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            output.append(pos)

        return output