class Solution:
    def maxOperations(self, nums):
        ZERO = 0
        ONE = 1
        TWO = ONE + ONE
        THREE = TWO + ONE

        def dfs(x, y, threshold, cache):
            if x >= y:
                return ZERO
            if (x, y, threshold) in cache:
                return cache[(x, y, threshold)]

            highestCount = ZERO
            sumLeftPair = nums[x] + nums[x + ONE]
            sumRightPair = nums[y] + nums[y - ONE]
            sumOuterPair = nums[x] + nums[y]

            if sumLeftPair == threshold:
                countAfterLeft = dfs(x + TWO, y, threshold, cache)
                if highestCount < ONE + countAfterLeft:
                    highestCount = ONE + countAfterLeft

            if sumRightPair == threshold:
                countAfterRight = dfs(x, y - TWO, threshold, cache)
                if highestCount < ONE + countAfterRight:
                    highestCount = ONE + countAfterRight

            if sumOuterPair == threshold:
                countAfterOuter = dfs(x + ONE, y - ONE, threshold, cache)
                if highestCount < ONE + countAfterOuter:
                    highestCount = ONE + countAfterOuter

            cache[(x, y, threshold)] = highestCount
            return highestCount

        lenNums = len(nums)
        candidateOne = ONE + dfs(TWO, lenNums - ONE, nums[ZERO] + nums[ONE], {})
        candidateTwo = ONE + dfs(ZERO, lenNums - THREE, nums[lenNums - TWO] + nums[lenNums - ONE], {})
        candidateThree = ONE + dfs(ONE, lenNums - TWO, nums[ZERO] + nums[lenNums - ONE], {})

        return max(candidateOne, candidateTwo, candidateThree)