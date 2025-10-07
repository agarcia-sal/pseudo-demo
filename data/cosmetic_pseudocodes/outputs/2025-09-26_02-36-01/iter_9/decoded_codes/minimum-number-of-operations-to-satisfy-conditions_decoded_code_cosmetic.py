class Solution:
    def minimumOperations(self, matrix):
        def areDifferent(x, y):
            return x != y

        def assignValue(row, col, value):
            matrix[row][col] = value

        def findReplacement(excludeValue):
            for candidate in range(10):
                if candidate != excludeValue:
                    return candidate
            return 0

        totalOps = 0
        numRows = len(matrix)
        numCols = len(matrix[0]) if numRows > 0 else 0

        columnIndex = 0
        while columnIndex < numCols:
            rowIndex = 0
            while rowIndex < numRows - 1:
                if areDifferent(matrix[rowIndex][columnIndex], matrix[rowIndex + 1][columnIndex]):
                    totalOps += 1
                    assignValue(rowIndex + 1, columnIndex, matrix[rowIndex][columnIndex])
                rowIndex += 1

            scanRow = 0
            while scanRow < numRows:
                if (columnIndex < numCols - 1) and (matrix[scanRow][columnIndex] == matrix[scanRow][columnIndex + 1]):
                    totalOps += 1
                    matrix[scanRow][columnIndex + 1] = findReplacement(matrix[scanRow][columnIndex])
                scanRow += 1

            columnIndex += 1

        return totalOps