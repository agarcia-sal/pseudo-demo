class Solution:
    def minChanges(self, nums, k):
        tally = [0] * (k + 2)
        lengthNums = len(nums)
        pointer = 0
        while pointer < lengthNums // 2:
            firstNum = nums[pointer]
            secondNum = nums[lengthNums - pointer - 1]
            if firstNum > secondNum:
                firstNum, secondNum = secondNum, firstNum
            tally[0] += 1
            tally[secondNum - firstNum] -= 1
            tally[secondNum - firstNum + 1] += 1
            max_val = max(secondNum, k - firstNum)
            tally[max_val + 1] -= 1
            tally[max_val + 2] += 1
            pointer += 1
        runningSum = 0
        minResult = float('inf')
        for val in tally:
            runningSum += val
            if runningSum < minResult:
                minResult = runningSum
        return minResult