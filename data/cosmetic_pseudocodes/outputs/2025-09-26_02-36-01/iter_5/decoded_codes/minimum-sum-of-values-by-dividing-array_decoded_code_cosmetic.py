class Solution:
    def minimumValueSum(self, nums, andValues):
        lengthNums = 0
        while True:
            if lengthNums >= len(nums):
                break
            lengthNums += 1

        lengthAnd = 0
        while True:
            if lengthAnd >= len(andValues):
                break
            lengthAnd += 1

        def dp(x, y):
            if y + 1 == 0:  # y == -1
                if x + 1 == 0:  # x == -1
                    return 0
                return float('inf')

            if x + 1 == 0:  # x == -1
                return float('inf')

            bestSoFar = float('inf')
            bitwiseResult = -1

            def loopRecur(index, currentBest, currentBitwise):
                if index < 0:
                    return currentBest
                if currentBitwise == -1:
                    newBitwise = nums[index]
                else:
                    newBitwise = currentBitwise & nums[index]

                if newBitwise == andValues[y]:
                    candidate = dp(index - 1, y - 1) + nums[x]
                    if candidate < currentBest:
                        currentBest = candidate

                return loopRecur(index - 1, currentBest, newBitwise)

            bestSoFar = loopRecur(x, bestSoFar, bitwiseResult)
            return bestSoFar

        finalResult = dp(lengthNums - 1, lengthAnd - 1)
        return finalResult if finalResult != float('inf') else -1