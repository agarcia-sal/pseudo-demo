from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1

        dp = [dict() for _ in range(n)]
        max_length = 1

        for i in range(n):
            for j in range(i):
                remainder = (nums[i] + nums[j]) % k
                if remainder in dp[j]:
                    dp[i][remainder] = dp[j][remainder] + 1
                else:
                    dp[i][remainder] = 2

                if dp[i][remainder] > max_length:
                    max_length = dp[i][remainder]

        return max_length