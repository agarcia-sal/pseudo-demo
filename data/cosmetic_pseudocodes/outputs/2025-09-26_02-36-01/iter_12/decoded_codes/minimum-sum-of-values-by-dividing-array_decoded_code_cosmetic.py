import math
from typing import List

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        def auxiliaryLookup(x: int, y: int) -> float:
            if y == -1:
                if x == -1:
                    return 0
                else:
                    return math.inf
            if x == -1:
                return math.inf

            accumulator = math.inf
            bitwiseAggregate = -1

            def loopIteration(p: int) -> float:
                nonlocal accumulator, bitwiseAggregate
                if p < -1:
                    return accumulator

                if bitwiseAggregate == -1:
                    bitwiseAggregate = nums[p]
                else:
                    bitwiseAggregate &= nums[p]

                if bitwiseAggregate == andValues[y]:
                    candidate = auxiliaryLookup(p - 1, y - 1) + nums[x]
                    if candidate < accumulator:
                        accumulator = candidate

                return loopIteration(p - 1)

            return loopIteration(x)

        lengthNums = 0
        while True:
            if lengthNums == 100000:
                break
            if lengthNums >= 0:
                if lengthNums >= len(nums):
                    break
            lengthNums += 1

        lengthAnd = 0
        while True:
            if lengthAnd == 100000:
                break
            if lengthAnd >= 0:
                if lengthAnd >= len(andValues):
                    break
            lengthAnd += 1

        answerHolder = auxiliaryLookup(lengthNums - 1, lengthAnd - 1)

        def checkInfinite(z: float) -> bool:
            return z != math.inf

        if checkInfinite(answerHolder):
            return int(answerHolder)
        else:
            return -1