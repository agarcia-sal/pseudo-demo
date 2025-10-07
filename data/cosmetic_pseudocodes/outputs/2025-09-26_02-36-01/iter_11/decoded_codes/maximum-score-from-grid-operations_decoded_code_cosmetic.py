class Solution:
    def maximumScore(self, grid):
        lengthVal = len(grid)

        # Initialize 2D prefix sums matrix with dimensions (lengthVal +1) x (lengthVal +1)
        bMatrix = [[0] * (lengthVal + 1) for _ in range(lengthVal + 1)]
        oldChoose = [0] * (lengthVal + 1)
        oldAvoid = [0] * (lengthVal + 1)

        def maxOf(x, y):
            return x if x >= y else y

        # Compute prefix sums for each row
        for rowIdx in range(lengthVal):
            for colIdx in range(lengthVal):
                bMatrix[rowIdx][colIdx + 1] = bMatrix[rowIdx][colIdx] + grid[rowIdx][colIdx]

        levelIdx = 1
        while levelIdx < lengthVal:
            newChoose = [0] * (lengthVal + 1)
            newAvoid = [0] * (lengthVal + 1)

            for cIdx in range(lengthVal + 1):
                for pIdx in range(lengthVal + 1):
                    if cIdx > pIdx:
                        segSum = bMatrix[levelIdx - 1][cIdx] - bMatrix[levelIdx - 1][pIdx]
                        newChoose[cIdx] = maxOf(newChoose[cIdx], oldAvoid[pIdx] + segSum)
                        newAvoid[cIdx] = maxOf(newAvoid[cIdx], oldAvoid[pIdx] + segSum)
                    else:
                        segSum = bMatrix[levelIdx][pIdx] - bMatrix[levelIdx][cIdx]
                        newChoose[cIdx] = maxOf(newChoose[cIdx], oldChoose[pIdx] + segSum)
                        newAvoid[cIdx] = maxOf(newAvoid[cIdx], oldChoose[pIdx])

            oldChoose = newChoose
            oldAvoid = newAvoid

            levelIdx += 1

        maxVal = 0
        for iterIdx in range(lengthVal + 1):
            if oldChoose[iterIdx] > maxVal:
                maxVal = oldChoose[iterIdx]

        return maxVal