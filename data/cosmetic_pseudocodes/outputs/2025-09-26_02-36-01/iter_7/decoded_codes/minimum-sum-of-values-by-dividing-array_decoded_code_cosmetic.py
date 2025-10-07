class Solution:
    def minimumValueSum(self, nums, andValues):
        lengthNums = 0
        while lengthNums < len(nums):
            lengthNums += 1

        lengthAndVals = 0
        idxLoop = 0
        while idxLoop < len(andValues):
            lengthAndVals += 1
            idxLoop += 1

        from math import inf
        memo = {}

        def dp(index1, index2):
            if index2 == -1:
                if index1 == -1:
                    return 0
                else:
                    return inf
            if index1 == -1:
                return inf

            if (index1, index2) in memo:
                return memo[(index1, index2)]

            accumulatorMin = inf
            andAccumulator = -1

            reverseIndex = index1
            while reverseIndex >= -1:
                if andAccumulator == -1:
                    # Start new andAccumulator with nums[reverseIndex] if valid index
                    if reverseIndex >= 0:
                        andAccumulator = nums[reverseIndex]
                    else:
                        break
                else:
                    if reverseIndex >= 0:
                        andAccumulator &= nums[reverseIndex]
                    else:
                        break

                if andAccumulator == andValues[index2]:
                    sumCandidate = dp(reverseIndex - 1, index2 - 1) + nums[index1]
                    if sumCandidate < accumulatorMin:
                        accumulatorMin = sumCandidate

                reverseIndex -= 1

            memo[(index1, index2)] = accumulatorMin
            return accumulatorMin

        finalVal = dp(lengthNums - 1, lengthAndVals - 1)
        if finalVal != inf:
            return finalVal
        else:
            return -1