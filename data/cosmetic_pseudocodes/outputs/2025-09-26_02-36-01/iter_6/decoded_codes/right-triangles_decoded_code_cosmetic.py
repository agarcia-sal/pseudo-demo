class Solution:
    def numberOfRightTriangles(self, grid):
        def addValues(arr, omitIndex):
            def helper(idx, acc):
                if idx >= len(arr):
                    return acc
                if idx != omitIndex:
                    return helper(idx + 1, acc + arr[idx])
                else:
                    return helper(idx + 1, acc)
            return helper(0, 0)

        total_triangles = 0
        total_rows = len(grid)
        total_cols = len(grid[0])

        def processRow(rowIdx, accum):
            if rowIdx >= total_rows:
                return accum

            def processCol(colIdx, accumInner):
                if colIdx >= total_cols:
                    return accumInner

                if grid[rowIdx][colIdx] == 1:
                    horizontal_sum = addValues(grid[rowIdx], colIdx)

                    def accumulateColumn(rIdx, accVert):
                        if rIdx >= total_rows:
                            return accVert
                        if rIdx != rowIdx:
                            return accumulateColumn(rIdx + 1, accVert + grid[rIdx][colIdx])
                        else:
                            return accumulateColumn(rIdx + 1, accVert)
                    vertical_sum = accumulateColumn(0, 0)

                    current_add = horizontal_sum * vertical_sum
                    return processCol(colIdx + 1, accumInner + current_add)
                else:
                    return processCol(colIdx + 1, accumInner)

            newAccum = processCol(0, accum)
            return processRow(rowIdx + 1, newAccum)

        return processRow(0, total_triangles)