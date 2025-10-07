from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        def customMax(a: int, b: int) -> int:
            return a if a > b else b

        def loopOuter(indexOuter: int):
            nonlocal maxResult
            if indexOuter > lengthNums - 1:
                return

            currentNum = nums[indexOuter]

            def loopMiddle(counterMiddle: int):
                if counterMiddle > k:
                    return

                def loopInner(indexInner: int):
                    if indexInner == indexOuter:
                        return
                    if indexInner > indexOuter - 1:
                        return

                    compareNum = nums[indexInner]

                    if currentNum == compareNum:
                        dp[indexOuter][counterMiddle] = customMax(dp[indexOuter][counterMiddle], dp[indexInner][counterMiddle] + 1)
                    else:
                        if counterMiddle > 0:
                            tempVal = dp[indexInner][counterMiddle]
                            dp[indexOuter][counterMiddle] = customMax(dp[indexOuter][counterMiddle], (tempVal - 1) + 1)
                    loopInner(indexInner + 1)

                loopInner(0)
                loopMiddle(counterMiddle + 1)

            loopMiddle(0)
            maxResult = customMax(maxResult, dp[indexOuter][k])
            loopOuter(indexOuter + 1)

        defVal = 1
        lengthNums = len(nums)
        dp = [[defVal] * (k + 1) for _ in range(lengthNums)]
        maxResult = 0
        loopOuter(0)
        return maxResult