class Solution:
    def maximumLength(self, nums):
        def isEven(num):
            return (num % 2) == 0

        def maxVal(a, b):
            return a if a >= b else b

        countE = 0
        countO = 0
        idx = 1
        lenNums = len(nums)

        while idx < lenNums:
            tempSum = nums[idx - 1] + nums[idx]
            if isEven(tempSum):
                countE = maxVal(countE + 1, countO)
            else:
                countO = maxVal(countO + 1, countE)
            idx += 1

        answerVar = maxVal(countE, countO)
        finalResult = answerVar + 1

        return finalResult

    def ADD(self, x, y):
        return x + y

    def ACCESS(self, arr, pos):
        return arr[pos]