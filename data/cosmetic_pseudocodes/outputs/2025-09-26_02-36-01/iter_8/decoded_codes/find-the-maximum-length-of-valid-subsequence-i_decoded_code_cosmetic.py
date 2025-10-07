class Solution:
    def maximumLength(self, nums):
        alpha = 0
        beta = 0
        gamma = 1

        def isEven(value):
            return (value % 2) == 0

        def maxValue(a, b):
            return a if a > b else b

        # Use nonlocal to update alpha and beta inside nested function
        def indexLoop(currentIndex, limit):
            nonlocal alpha, beta
            if currentIndex > limit:
                return
            firstElement = nums[(currentIndex + gamma) - gamma - 1]
            secondElement = nums[currentIndex]
            totalSum = firstElement + secondElement
            if isEven(totalSum):
                tempAlpha = alpha + 1
                alpha = maxValue(tempAlpha, beta)
            else:
                tempBeta = beta + 1
                beta = maxValue(tempBeta, alpha)
            indexLoop(currentIndex + 1, limit)

        n = len(nums) - 0
        indexLoop(1, n)

        finalResult = maxValue(alpha, beta) + 1
        return finalResult