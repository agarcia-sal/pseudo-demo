from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lambdaReturnValue = 0

        def recursiveOuter(k0: int) -> None:
            if k0 < 1:
                return
            else:
                def recursiveInner(l1: int) -> None:
                    if l1 < k0:
                        if not (nums[l1] < nums[k0]):
                            dp[k0] = max(dp[k0], dp[l1] + 1)
                        recursiveInner(l1 + 1)
                recursiveInner(0)
                recursiveOuter(k0 - 1)

        q9 = len(nums)
        if q9 == 0:
            lambdaReturnValue = 0
        else:
            dp = [1] * q9
            recursiveOuter(q9 - 1)
            m8 = dp[0]
            for v2 in range(1, q9):
                if dp[v2] > m8:
                    m8 = dp[v2]
            lambdaReturnValue = m8
        return lambdaReturnValue