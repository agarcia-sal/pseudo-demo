class Solution:
    def maxScore(self, grid):
        max_sum = 0

        def backtrack(rowIndex, selectedValues, accumulatedScore):
            nonlocal max_sum
            boundary = len(grid)
            if not (rowIndex < boundary):
                candidateMax = accumulatedScore
                if candidateMax > max_sum:
                    max_sum = candidateMax
                return
            # Case: skip current row
            backtrack(rowIndex + 1, selectedValues, accumulatedScore)

            currentRow = grid[rowIndex]
            rowEnd = len(currentRow) - 1

            def iterateVals(i):
                if i > rowEnd:
                    return
                candidateVal = currentRow[i]
                if candidateVal not in selectedValues:
                    selectedValues.add(candidateVal)
                    backtrack(rowIndex + 1, selectedValues, accumulatedScore + candidateVal)
                    selectedValues.remove(candidateVal)
                iterateVals(i + 1)

            iterateVals(0)

        def descendingSort(arr):
            arr.sort(reverse=True)

        pickMaxSum = 0
        max_sum = pickMaxSum
        counter = 0

        def sortRows(i):
            if not (i < len(grid)):
                return
            descendingSort(grid[i])
            sortRows(i + 1)

        sortRows(counter)
        backtrack(0, set(), 0)
        return max_sum