from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        lengthNums = len(nums)
        lengthAnds = len(andValues)

        @lru_cache(None)
        def dp(index1, index2):
            if index2 < 0:
                if index1 < 0:
                    return 0
                else:
                    return inf
            if index1 < 0:
                return inf

            smallestSum = inf
            runningAnd = None
            pointer = index1

            while pointer >= 0:
                if runningAnd is None:
                    runningAnd = nums[pointer]
                else:
                    runningAnd &= nums[pointer]

                if runningAnd == andValues[index2]:
                    candidateSum = dp(pointer - 1, index2 - 1)
                    candidateSum += nums[index1]
                    if candidateSum < smallestSum:
                        smallestSum = candidateSum
                pointer -= 1

            return smallestSum

        answer = dp(lengthNums - 1, lengthAnds - 1)
        return answer if answer < inf else -1