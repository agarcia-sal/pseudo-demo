class Solution:
    def sumOfPower(self, nums, k):
        CONST_MOD = 10**9 + 7
        lengthNums = len(nums)

        dpTable = [[0] * (k + 1) for _ in range(lengthNums + 1)]
        dpTable[0][0] = 1

        for idxOuter in range(1, lengthNums + 1):
            neededVal = nums[idxOuter - 1]
            for idxInner in range(k + 1):
                dpTable[idxOuter][idxInner] = dpTable[idxOuter - 1][idxInner]
                if idxInner >= neededVal:
                    dpTable[idxOuter][idxInner] += dpTable[idxOuter - 1][idxInner - neededVal]
                dpTable[idxOuter][idxInner] %= CONST_MOD

        aggregatePower = 0
        upperLimit = (1 << lengthNums) - 1

        subsetIndicator = 1
        while subsetIndicator <= upperLimit:
            partialSum = 0
            elementCount = 0
            bitIndex = 0

            while bitIndex < lengthNums:
                if ((subsetIndicator >> bitIndex) & 1) == 1:
                    partialSum += nums[bitIndex]
                    elementCount += 1
                bitIndex += 1

            if partialSum == k:
                incrementVal = pow(2, lengthNums - elementCount, CONST_MOD)
                aggregatePower = (aggregatePower + incrementVal) % CONST_MOD

            subsetIndicator += 1

        return aggregatePower