from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        arr = [0] * m
        idx = m - 2

        while idx >= 0:
            curr_max = 0

            def inner_fun(k):
                nonlocal curr_max
                if k == m:
                    return
                val = (k - idx) * nums[k]
                temp = val + arr[k]
                if curr_max < temp:
                    curr_max = temp
                inner_fun(k + 1)

            inner_fun(idx + 1)
            arr[idx] = curr_max
            idx -= 1

        return arr[0]