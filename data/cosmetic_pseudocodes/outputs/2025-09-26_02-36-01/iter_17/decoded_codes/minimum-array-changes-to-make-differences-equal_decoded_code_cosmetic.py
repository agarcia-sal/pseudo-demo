class Solution:
    def minChanges(self, nums, k):
        deltaArr = [0] * (k + 2)
        lenNums = len(nums)
        index = 0
        half_len = lenNums // 2

        while index < half_len:
            firstVal = nums[index]
            secondVal = nums[lenNums - 1 - index]

            # Ensure swapped1 <= swapped2
            if firstVal <= secondVal:
                swapped1, swapped2 = firstVal, secondVal
            else:
                swapped1, swapped2 = secondVal, firstVal

            deltaArr[0] += 1
            deltaArr[swapped2 - swapped1] -= 1
            deltaArr[swapped2 - swapped1 + 1] += 1

            maxVal = swapped2
            diffVal = k - swapped1
            if maxVal < diffVal:
                maxVal = diffVal

            deltaArr[maxVal + 1] -= 1
            deltaArr[maxVal + 2] += 1

            index += 1

        runningSum = 0
        minRes = float('inf')
        for iterIdx in range(k + 2):
            runningSum += deltaArr[iterIdx]
            if runningSum < minRes:
                minRes = runningSum

        return minRes