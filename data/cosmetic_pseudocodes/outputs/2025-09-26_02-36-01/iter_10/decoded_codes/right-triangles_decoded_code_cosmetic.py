class Solution:
    def numberOfRightTriangles(self, grid):
        L0 = len(grid)
        L1 = len(grid[0])
        total_triangles = 0  # Corresponds to R in pseudocode outside (renamed for clarity)

        def SummateExceptColumn(currRowIndex, excludedCol):
            sum_val = 0
            idx = 0
            while idx < L1:
                if idx != excludedCol:
                    sum_val += grid[currRowIndex][idx]
                idx += 1
            return sum_val

        def SummateExceptRow(excludedRow, currColIndex):
            sum_val = 0
            idx = 0
            while idx < L0:
                if idx != excludedRow:
                    sum_val += grid[idx][currColIndex]
                idx += 1
            return sum_val

        OuterIndex = 0
        while OuterIndex < L0:
            InnerIndex = 0
            while InnerIndex < L1:
                if grid[OuterIndex][InnerIndex] == 1:
                    A = SummateExceptColumn(OuterIndex, InnerIndex)
                    R = SummateExceptRow(OuterIndex, InnerIndex)
                    total_triangles += A * R
                InnerIndex += 1
            OuterIndex += 1

        return total_triangles