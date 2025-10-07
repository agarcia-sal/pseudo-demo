class Solution:
    def maximumScore(self, grid):
        lengthVal = len(grid)
        # cumSum dimensions: (lengthVal) x (lengthVal + 1)
        cumSum = [[0] * (lengthVal + 1) for _ in range(lengthVal)]
        lastChoose = [0] * (lengthVal + 1)
        lastIgnore = [0] * (lengthVal + 1)

        for colIndex in range(lengthVal):
            for rowIndex in range(lengthVal):
                cumIndex1 = rowIndex + 1
                cumIndex2 = colIndex
                cumSum[cumIndex2][cumIndex1] = cumSum[cumIndex2][rowIndex] + grid[rowIndex][colIndex]

        for colPointer in range(1, lengthVal):
            currentChoose = [0] * (lengthVal + 1)
            currentIgnore = [0] * (lengthVal + 1)

            for currIndex in range(lengthVal + 1):
                for prevIndex in range(lengthVal + 1):
                    if currIndex > prevIndex:
                        diffCalc = cumSum[colPointer - 1][currIndex] - cumSum[colPointer - 1][prevIndex]
                        currentChoose[currIndex] = max(currentChoose[currIndex], lastIgnore[prevIndex] + diffCalc)
                        currentIgnore[currIndex] = max(currentIgnore[currIndex], lastIgnore[prevIndex] + diffCalc)
                    else:
                        diffAlt = cumSum[colPointer][prevIndex] - cumSum[colPointer][currIndex]
                        currentChoose[currIndex] = max(currentChoose[currIndex], lastChoose[prevIndex] + diffAlt)
                        currentIgnore[currIndex] = max(currentIgnore[currIndex], lastChoose[prevIndex])

            lastChoose = currentChoose
            lastIgnore = currentIgnore

        maxResult = lastChoose[0]
        for idx in range(1, lengthVal + 1):
            if lastChoose[idx] > maxResult:
                maxResult = lastChoose[idx]

        return maxResult