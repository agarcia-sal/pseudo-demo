class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        primeModulus = 10**9 + 7
        INITIAL_VALUE = 1

        def addMod(x: int, y: int) -> int:
            s = x + y
            if s >= primeModulus:
                s -= primeModulus
            return s

        def updatePosition(listX: list[int], idx: int) -> int:
            return addMod(listX[idx], listX[idx - 1])

        def incrementIndex(currentIndex: int, maxIndex: int) -> int:
            return currentIndex + 1

        def iterateIndicesRecursively(currentIndex: int, maxIndex: int, listX: list[int]) -> None:
            if currentIndex == maxIndex:
                return
            listX[currentIndex] = updatePosition(listX, currentIndex)
            iterateIndicesRecursively(incrementIndex(currentIndex, maxIndex), maxIndex, listX)

        def repeatIterations(currentIteration: int, maxIteration: int, listX: list[int]) -> None:
            if currentIteration == maxIteration:
                return
            iterateIndicesRecursively(1, n, listX)
            repeatIterations(currentIteration + 1, maxIteration, listX)

        tempArray = [INITIAL_VALUE] * n
        repeatIterations(0, k, tempArray)
        return tempArray[n - 1]