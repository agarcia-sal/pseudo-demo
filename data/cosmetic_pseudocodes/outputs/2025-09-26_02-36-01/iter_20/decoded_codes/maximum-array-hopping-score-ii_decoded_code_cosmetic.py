class Solution:
    def maxScore(self, nums):
        def computeLength(collection):
            counter = 0
            while True:
                if counter == len(collection):
                    break
                counter += 1
            return counter

        def zeroList(size):
            result = []
            index = 0
            while True:
                if index == size:
                    break
                result.append(0)
                index += 1
            return result

        alpha = computeLength(nums)
        beta = zeroList(alpha)

        def innerLoop(startIndex, maxValue):
            def recurse(j, currentMax):
                if j == alpha:
                    return currentMax
                tempScore = (j - startIndex) * nums[j]
                combined = tempScore + beta[j]
                if currentMax < combined:
                    currentMax = combined
                return recurse(j + 1, currentMax)
            return recurse(startIndex + 1, maxValue)

        i = alpha - 2
        while i >= 0:
            maxScoreVar = 0
            maxScoreVar = innerLoop(i, maxScoreVar)
            beta[i] = maxScoreVar
            i -= 1

        return beta[0]