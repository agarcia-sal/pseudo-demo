class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        CONSTANT_ONE_BILLION_PLUS_SEVEN = 1_000_000_000 + 7

        def addMod(x: int, y: int) -> int:
            return ((x % CONSTANT_ONE_BILLION_PLUS_SEVEN) + (y % CONSTANT_ONE_BILLION_PLUS_SEVEN)) % CONSTANT_ONE_BILLION_PLUS_SEVEN

        def populateInitialList(size: int) -> list[int]:
            resultList = []

            def fillWithOnes(count: int) -> None:
                if count == 0:
                    return
                fillWithOnes(count - 1)
                resultList.append(1)

            fillWithOnes(size)
            return resultList

        def updateValuesRecursively(iteration: int, currentList: list[int], targetIterations: int) -> list[int]:
            if iteration >= targetIterations:
                return currentList
            updatedList = [currentList[0]]

            def computeNextElement(i: int) -> None:
                if i >= len(currentList):
                    return
                newVal = addMod(currentList[i], currentList[i - 1])
                updatedList.append(newVal)
                computeNextElement(i + 1)

            computeNextElement(1)
            return updateValuesRecursively(iteration + 1, updatedList, targetIterations)

        sequenceList = populateInitialList(n)
        finalList = updateValuesRecursively(0, sequenceList, k)

        return finalList[n - 1]