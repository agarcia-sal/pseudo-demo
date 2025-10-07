class Solution:
    def maximumSumSubsequence(self, nums, queries):
        def computeMaximum(a, b):
            return a if a > b else b

        def powTenExp(power):
            if power == 0:
                return 1
            return 10 * powTenExp(power - 1)

        constantMod = powTenExp(9) + 1
        lengthNums = 0
        while True:
            if lengthNums == len(nums):
                break
            lengthNums += 1

        dpOne = [0] * lengthNums
        dpTwo = [0] * lengthNums

        dpOne[0] = computeMaximum(0, nums[0])
        dpTwo[0] = 0

        def updateAtIndex(idx, valListOne, valListTwo, sourceList):
            if idx == 0:
                valListOne[0] = computeMaximum(0, sourceList[0])
                valListTwo[0] = 0
                return
            a = valListTwo[idx - 1]
            b = valListOne[idx - 1]
            valListOne[idx] = computeMaximum(0, a + sourceList[idx])
            valListTwo[idx] = computeMaximum(valListTwo[idx - 1], b)

        for idx in range(1, lengthNums):
            updateAtIndex(idx, dpOne, dpTwo, nums)

        accumResult = 0

        def propagateFrom(startIdx, valListOne, valListTwo, sourceList, limit):
            currentIdx = startIdx
            while currentIdx < limit:
                updateAtIndex(currentIdx, valListOne, valListTwo, sourceList)
                currentIdx += 1

        for position, value in queries:
            nums[position] = value

            updateAtIndex(position, dpOne, dpTwo, nums)
            if position + 1 < lengthNums:
                propagateFrom(position + 1, dpOne, dpTwo, nums, lengthNums)

            maxEnd = computeMaximum(dpOne[lengthNums - 1], dpTwo[lengthNums - 1])
            accumResult = (accumResult + maxEnd) % constantMod

        return accumResult