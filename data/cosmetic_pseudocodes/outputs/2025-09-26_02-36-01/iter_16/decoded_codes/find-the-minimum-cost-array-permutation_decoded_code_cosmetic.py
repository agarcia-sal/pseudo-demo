class Solution:
    def findPermutation(self, nums):
        lengthOfNums = len(nums)
        ans = []

        def dfs(currentMask, previousIndex):
            if currentMask == (1 << lengthOfNums) - 1:
                return abs(previousIndex - nums[0])
            minimalValue = float('inf')
            for indexIterator in range(lengthOfNums):
                if ((currentMask >> indexIterator) & 1) == 0:
                    tempCalc = abs(previousIndex - nums[indexIterator]) + dfs(currentMask | (1 << indexIterator), indexIterator)
                    if tempCalc < minimalValue:
                        minimalValue = tempCalc
            return minimalValue

        def g(currentMask, previousIndex):
            ans.append(previousIndex)
            if currentMask == (1 << lengthOfNums) - 1:
                return
            resultValue = dfs(currentMask, previousIndex)
            for newCur in range(lengthOfNums):
                if ((currentMask >> newCur) & 1) == 0:
                    candidateResult = abs(previousIndex - nums[newCur]) + dfs(currentMask | (1 << newCur), newCur)
                    if candidateResult == resultValue:
                        g(currentMask | (1 << newCur), newCur)
                        break

        g(1, 0)
        return ans