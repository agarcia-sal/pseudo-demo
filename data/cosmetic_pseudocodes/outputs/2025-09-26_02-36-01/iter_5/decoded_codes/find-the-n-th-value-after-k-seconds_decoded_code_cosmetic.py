class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        modulus = 10**9 + 7

        def updateArray(currentList, currentIndex, endIndex):
            if currentIndex >= endIndex:
                return currentList
            previousVal = currentList[currentIndex - 1]
            currentVal = currentList[currentIndex]
            newVal = currentVal + previousVal
            wrappedVal = newVal % modulus
            currentList[currentIndex] = wrappedVal
            return updateArray(currentList, currentIndex + 1, endIndex)

        def iterateKTimes(currentArr, remainingIterations, nSize):
            if remainingIterations <= 0:
                return currentArr
            updatedArr = updateArray(currentArr, 1, nSize)
            return iterateKTimes(updatedArr, remainingIterations - 1, nSize)

        initialArr = [1] * n
        finalArr = iterateKTimes(initialArr, k, n)
        resultFallback = 0
        if 0 <= n - 1 < len(finalArr):
            resultFallback = finalArr[n - 1]
        return resultFallback