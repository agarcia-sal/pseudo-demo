class Solution:
    def sumOfPower(self, nums, k):
        MOD_CONST = 10**9 + 7
        sz = len(nums)
        dpTable = []
        rowTemplate = [0] * (k + 1)
        for _ in range(sz + 1):
            dpTable.append(rowTemplate[:])

        dpTable[0][0] = 1

        for outerIdx in range(1, sz + 1):
            for innerIdx in range(k + 1):
                dpTable[outerIdx][innerIdx] = dpTable[outerIdx - 1][innerIdx]
                if innerIdx >= nums[outerIdx - 1]:
                    dpTable[outerIdx][innerIdx] = (dpTable[outerIdx][innerIdx] + dpTable[outerIdx - 1][innerIdx - nums[outerIdx - 1]]) % MOD_CONST
                else:
                    dpTable[outerIdx][innerIdx] %= MOD_CONST  # Ensure mod after assignment

        totalPower = 0
        limitVal = (1 << sz) - 1
        subsetCounter = 1

        while subsetCounter <= limitVal:
            aggregateSum = 0
            elementsCount = 0
            bitPointer = 0

            while bitPointer < sz:
                if ((subsetCounter >> bitPointer) & 1) == 1:
                    aggregateSum += nums[bitPointer]
                    elementsCount += 1
                bitPointer += 1

            if aggregateSum == k:
                exponentVal = 1 << (sz - elementsCount)
                totalPower = (totalPower + exponentVal) % MOD_CONST

            subsetCounter += 1

        return totalPower