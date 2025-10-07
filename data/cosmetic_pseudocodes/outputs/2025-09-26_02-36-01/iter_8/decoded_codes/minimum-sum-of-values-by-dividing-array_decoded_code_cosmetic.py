class Solution:
    def minimumValueSum(self, nums, andValues):
        totalCount = len(nums)
        boundCount = len(andValues)
        infVal = float('inf')
        sentinelVal = -1
        zeroVal = 0

        from functools import lru_cache

        @lru_cache(None)
        def dp(index1, index2):
            if index2 == sentinelVal:
                if index1 == sentinelVal:
                    return zeroVal
                else:
                    return infVal
            if index1 == sentinelVal:
                return infVal

            answerHolder = infVal
            accumulatorAnd = sentinelVal
            iterator = index1

            while iterator >= sentinelVal:
                if accumulatorAnd == sentinelVal:
                    accumulatorAnd = nums[iterator]
                else:
                    accumulatorAnd &= nums[iterator]

                if accumulatorAnd == andValues[index2]:
                    candidateVal = dp(iterator - 1, index2 - 1)
                    candidateValAdjusted = candidateVal + nums[index1]
                    if candidateValAdjusted < answerHolder:
                        answerHolder = candidateValAdjusted

                iterator -= 1

            return answerHolder

        finalResult = dp(totalCount - 1, boundCount - 1)
        return finalResult if finalResult != infVal else -1