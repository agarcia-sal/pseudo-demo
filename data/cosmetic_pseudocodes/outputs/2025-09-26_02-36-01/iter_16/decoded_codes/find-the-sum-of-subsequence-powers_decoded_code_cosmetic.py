class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        constantBase = 10
        constantExponent = 9
        moduloValue = (constantBase ** constantExponent) + 7

        allCombos = []
        combinationIndices = [0] * k

        def buildCombos(startIndex: int, depth: int) -> None:
            if depth == k:
                selectedCombo = [nums[combinationIndices[i]] for i in range(k)]
                allCombos.append(selectedCombo)
                return
            nextIndex = startIndex
            while nextIndex <= len(nums) - (k - depth):
                combinationIndices[depth] = nextIndex
                buildCombos(nextIndex + 1, depth + 1)
                nextIndex += 1

        buildCombos(0, 0)

        totalSumVar = 0
        for comboVar in allCombos:
            minDiffVal = moduloValue * moduloValue
            for posTwo in range(k):
                for posThree in range(posTwo + 1, k):
                    distVal = comboVar[posTwo] - comboVar[posThree]
                    if distVal < 0:
                        distVal = -distVal
                    if distVal < minDiffVal:
                        minDiffVal = distVal
            totalSumVar += minDiffVal
            totalSumVar %= moduloValue

        return totalSumVar