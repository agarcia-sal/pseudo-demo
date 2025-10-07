class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        modBase = 10**9 + 7
        accumulativeTotal = 0

        def absVal(x: int) -> int:
            return -x if x < 0 else x

        def generateCombinations(inputList: list[int], selectionCount: int) -> list[list[int]]:
            resultList = []

            def recHelper(startIndex: int, pathList: list[int]) -> None:
                if len(pathList) == selectionCount:
                    resultList.append(pathList)
                    return
                idx = startIndex
                while idx < len(inputList):
                    recHelper(idx + 1, pathList + [inputList[idx]])
                    idx += 1

            recHelper(0, [])
            return resultList

        combinationCollection = generateCombinations(nums, k)

        def computeMinDiff(values: list[int]) -> int:
            def innerLoopOuter(x: int, y: int, currentMin: int) -> int:
                if x >= len(values) - 1:
                    return currentMin
                elif y >= len(values):
                    return innerLoopOuter(x + 1, x + 2, currentMin)
                else:
                    diffToEvaluate = absVal(values[x] - values[y])
                    newMin = currentMin
                    if diffToEvaluate < currentMin:
                        newMin = diffToEvaluate
                    return innerLoopOuter(x, y + 1, newMin)

            return innerLoopOuter(0, 1, 1 << 30)

        def processCombinations(combinationIndex: int, accum: int) -> int:
            if combinationIndex >= len(combinationCollection):
                return accum
            else:
                minDifferenceVal = computeMinDiff(combinationCollection[combinationIndex])
                updatedSum = accum + minDifferenceVal
                moddedSum = updatedSum - ( (updatedSum // modBase) * modBase )
                return processCombinations(combinationIndex + 1, moddedSum)

        finalResult = processCombinations(0, accumulativeTotal)
        return finalResult