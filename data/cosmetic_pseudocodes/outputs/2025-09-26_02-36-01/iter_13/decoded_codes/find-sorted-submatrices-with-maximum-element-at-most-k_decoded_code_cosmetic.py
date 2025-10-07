class Solution:
    def countSubmatrices(self, grid, k):
        rowsCount = len(grid)
        colsCount = len(grid[0])
        totalCounter = 0

        def checkSubmatrixValidity(matrix):
            def checkRowValidity(row, idx):
                if idx == len(row):
                    return True
                if row[idx] > k:
                    return False
                return checkRowValidity(row, idx + 1)

            def validateRows(matrix, idx):
                if idx == len(matrix):
                    return True
                if not checkRowValidity(matrix[idx], 0):
                    return False
                return validateRows(matrix, idx + 1)

            return validateRows(matrix, 0)

        def verifySubmatrixSortedOrder(matrix):
            def checkRowOrder(row, position):
                if position == len(row):
                    return True
                if not (row[position] <= row[position - 1]):
                    return False
                return checkRowOrder(row, position + 1)

            def validateAllRows(matrix, index):
                if index == len(matrix):
                    return True
                if not checkRowOrder(matrix[index], 1):
                    return False
                return validateAllRows(matrix, index + 1)

            return validateAllRows(matrix, 0)

        def iterateY2(x1, y1, x2):
            nonlocal totalCounter
            y2Index = y1
            while y2Index < colsCount:
                extractedSubmatrix = []
                tempRowIndex = x1
                while tempRowIndex <= x2:
                    extractedSubmatrix.append(grid[tempRowIndex][y1 : y2Index + 1])
                    tempRowIndex += 1

                if checkSubmatrixValidity(extractedSubmatrix) and verifySubmatrixSortedOrder(extractedSubmatrix):
                    totalCounter += 1
                y2Index += 1

        def iterateX2(x1, y1):
            x2Index = x1
            while x2Index < rowsCount:
                iterateY2(x1, y1, x2Index)
                x2Index += 1

        def iterateY1(x1):
            y1Index = 0
            while y1Index < colsCount:
                iterateX2(x1, y1Index)
                y1Index += 1

        def iterateX1():
            x1Index = 0
            while x1Index < rowsCount:
                iterateY1(x1Index)
                x1Index += 1

        iterateX1()

        return totalCounter