class Solution:
    def minOperations(self, nums):
        lengthNums = len(nums)
        countOps = 0

        def recFlip(idx):
            nonlocal countOps
            if idx > lengthNums - 3:
                return
            currentVal = nums[idx]
            flippedCurrent = 1 - currentVal
            if currentVal == 0:
                nums[idx] = flippedCurrent
                nums[idx + 1] = 1 - nums[idx + 1]
                nums[idx + 2] = 1 - nums[idx + 2]
                countOps += 1
            recFlip(idx + 1)

        recFlip(0)

        penultimateVal = nums[lengthNums - 2]
        lastVal = nums[lengthNums - 1]
        isPenultimateZero = (penultimateVal == 0)
        isLastZero = (lastVal == 0)
        invalidEnd = False

        if isPenultimateZero or isLastZero:
            invalidEnd = True

        finalResult = -1 if invalidEnd else countOps
        return finalResult