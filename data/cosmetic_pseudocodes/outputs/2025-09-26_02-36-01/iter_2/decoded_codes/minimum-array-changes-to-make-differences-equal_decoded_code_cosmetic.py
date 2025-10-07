class Solution:
    def minChanges(self, nums, k):
        countArray = [0] * (k + 2)
        lengthNums = len(nums)
        idx = 0
        while idx < (lengthNums // 2):
            val1 = nums[idx]
            val2 = nums[lengthNums - idx - 1]
            if val1 > val2:
                val1, val2 = val2, val1
            countArray[0] += 1
            countArray[val2 - val1] -= 1
            countArray[(val2 - val1) + 1] += 1
            maxVal = val2 if val2 > (k - val1) else (k - val1)
            countArray[maxVal + 1] -= 1
            countArray[maxVal + 2] += 1
            idx += 1
        runningSum = 0
        minimumChanges = float('inf')
        pointer = 0
        while pointer < len(countArray):
            runningSum += countArray[pointer]
            if runningSum < minimumChanges:
                minimumChanges = runningSum
            pointer += 1
        return minimumChanges