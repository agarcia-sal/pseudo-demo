class Solution:
    def minChanges(self, nums, k):
        counts = [0] * (k + 2)
        lengthNums = len(nums)
        index = 0
        while index < lengthNums // 2:
            firstVal = nums[index]
            secondVal = nums[lengthNums - 1 - index]
            if firstVal <= secondVal:
                lowVal = firstVal
                highVal = secondVal
            else:
                lowVal = secondVal
                highVal = firstVal
            posZero = 0
            diffVal = highVal - lowVal
            diffPlusOne = diffVal + 1
            maxVal = highVal if highVal > (k - lowVal) else (k - lowVal)
            maxPlusOne = maxVal + 1
            maxPlusTwo = maxVal + 2

            counts[posZero] += 1
            counts[diffVal] -= 1
            counts[diffPlusOne] += 1
            if maxPlusOne < len(counts):
                counts[maxPlusOne] -= 1
            if maxPlusTwo < len(counts):
                counts[maxPlusTwo] += 1

            index += 1

        runningTotal = 0
        minimumResult = float('inf')
        for val in counts:
            runningTotal += val
            if runningTotal < minimumResult:
                minimumResult = runningTotal

        return minimumResult