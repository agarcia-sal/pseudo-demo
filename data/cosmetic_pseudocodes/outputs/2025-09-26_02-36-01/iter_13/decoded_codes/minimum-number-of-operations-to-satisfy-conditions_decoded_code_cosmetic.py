class Solution:
    def minimumOperations(self, grid):
        alpha = len(grid)
        beta = len(grid[0]) if alpha > 0 else 0
        delta = 0

        def nextDiffValue(curr):
            epsilon = 0
            while epsilon <= 9:
                if epsilon != curr:
                    return epsilon
                epsilon += 1
            return 0

        def fixColumns(colIdx, rowIdx, acc):
            if rowIdx >= alpha - 1:
                return acc
            if grid[rowIdx][colIdx] != grid[rowIdx + 1][colIdx]:
                return fixColumns(colIdx, rowIdx + 1, acc)
            grid[rowIdx + 1][colIdx] = grid[rowIdx][colIdx]
            return fixColumns(colIdx, rowIdx + 1, acc + 1)

        def modifyNextColumn(colIdx, rowIdx, acc):
            if rowIdx >= alpha:
                return acc
            if colIdx < beta - 1 and grid[rowIdx][colIdx] == grid[rowIdx][colIdx + 1]:
                grid[rowIdx][colIdx + 1] = nextDiffValue(grid[rowIdx][colIdx])
                return modifyNextColumn(colIdx, rowIdx + 1, acc + 1)
            return modifyNextColumn(colIdx, rowIdx + 1, acc)

        def iterateColumns(colIdx, acc):
            if colIdx >= beta:
                return acc
            updatedAcc = fixColumns(colIdx, 0, acc)
            newAcc = modifyNextColumn(colIdx, 0, updatedAcc)
            return iterateColumns(colIdx + 1, newAcc)

        return iterateColumns(0, delta)