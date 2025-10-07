from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 1:
            return 1

        dp = [{} for _ in range(length)]
        max_len = 1

        for current in range(length):
            for previous in range(current):
                sum_mod = (nums[current] + nums[previous]) % k

                if sum_mod in dp[previous]:
                    dp[current][sum_mod] = dp[previous][sum_mod] + 1
                else:
                    dp[current][sum_mod] = 2

                if dp[current][sum_mod] > max_len:
                    max_len = dp[current][sum_mod]

        return max_len