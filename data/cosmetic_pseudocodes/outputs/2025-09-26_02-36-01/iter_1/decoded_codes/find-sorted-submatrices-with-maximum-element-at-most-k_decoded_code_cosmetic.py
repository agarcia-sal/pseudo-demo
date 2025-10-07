class Solution:
    def countSubmatrices(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        def checkValues(matrix):
            for line in matrix:
                for item in line:
                    if item > k:
                        return False
            return True

        def checkDescending(matrix):
            for line in matrix:
                for idx in range(1, len(line)):
                    if line[idx] > line[idx - 1]:
                        return False
            return True

        for startRow in range(rows):
            for startCol in range(cols):
                for endRow in range(startRow, rows):
                    for endCol in range(startCol, cols):
                        extracted = []
                        for i in range(startRow, endRow + 1):
                            segment = grid[i][startCol:endCol + 1]
                            extracted.append(segment)
                        if checkValues(extracted) and checkDescending(extracted):
                            total += 1

        return total