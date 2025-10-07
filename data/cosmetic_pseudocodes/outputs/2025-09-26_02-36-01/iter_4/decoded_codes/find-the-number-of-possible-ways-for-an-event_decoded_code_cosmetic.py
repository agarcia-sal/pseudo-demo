class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        moduloValue = 10**9 + 7
        matrix = [[0] * (x + 1) for _ in range(n + 1)]
        matrix[0][0] = 1

        for rowIndex in range(1, n + 1):
            for colIndex in range(1, x + 1):
                prevRowSameCol = matrix[rowIndex - 1][colIndex]
                prevRowPrevCol = matrix[rowIndex - 1][colIndex - 1]

                termOne = prevRowSameCol * colIndex
                tempDiff = x - (colIndex - 1)
                termTwo = prevRowPrevCol * tempDiff

                sumTerms = termOne + termTwo
                remainder_mod = sumTerms - (sumTerms // moduloValue) * moduloValue

                matrix[rowIndex][colIndex] = remainder_mod

        resultAccumulator = 0
        powerMultiplier = 1
        for indexCounter in range(1, x + 1):
            powerMultiplier = (powerMultiplier * y) % moduloValue
            addend = (matrix[n][indexCounter] * powerMultiplier) % moduloValue
            resultAccumulator = (resultAccumulator + addend) % moduloValue

        return resultAccumulator