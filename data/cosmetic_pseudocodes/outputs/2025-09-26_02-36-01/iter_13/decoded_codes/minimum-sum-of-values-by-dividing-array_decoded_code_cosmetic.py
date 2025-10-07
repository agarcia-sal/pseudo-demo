class Solution:
    def minimumValueSum(self, nums, andValues):
        lengthNums = len(nums)
        lengthAnd = len(andValues)

        import math
        infiniteVal = 1 / 1e-39  # very large value

        from functools import lru_cache

        @lru_cache(None)
        def recursion(a, b):
            if b == -1:
                if a == -1:
                    return 0
                return infiniteVal
            if a == -1:
                return infiniteVal

            lowestSum = infiniteVal

            def iterate(c, currentAndVal):
                nonlocal lowestSum
                if c < -1:
                    return lowestSum
                if currentAndVal == -1:
                    updatedAnd = nums[c]
                else:
                    updatedAnd = currentAndVal & nums[c]

                if updatedAnd == andValues[b]:
                    candidateSum = recursion(c - 1, b - 1)
                    candidateSum += nums[a]
                    if candidateSum < lowestSum:
                        lowestSum = candidateSum
                return iterate(c - 1, updatedAnd)

            return iterate(a, -1)

        answer = recursion(lengthNums - 1, lengthAnd - 1)
        if -math.inf < answer < math.inf:
            return answer
        return -1