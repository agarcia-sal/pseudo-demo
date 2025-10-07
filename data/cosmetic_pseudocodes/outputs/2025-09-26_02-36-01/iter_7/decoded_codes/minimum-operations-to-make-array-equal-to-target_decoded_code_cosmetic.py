from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ZERO = 0
        ONE = ZERO + 1
        LENGTH = len(nums)
        accumulator = abs(target[ZERO] - nums[ZERO])

        iterator = ONE
        while iterator < LENGTH:
            diffCurr = target[iterator] - nums[iterator]
            diffPrev = target[iterator - ONE] - nums[iterator - ONE]

            if (diffCurr * diffPrev) > ZERO:
                diffAbsDelta = abs(abs(diffCurr) - abs(diffPrev))
                if diffAbsDelta > ZERO:
                    accumulator += diffAbsDelta
            else:
                accumulator += abs(diffCurr)
            iterator += ONE

        return accumulator