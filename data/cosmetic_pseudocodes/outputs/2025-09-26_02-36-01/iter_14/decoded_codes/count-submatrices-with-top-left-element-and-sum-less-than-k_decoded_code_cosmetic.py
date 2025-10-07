from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        def addValues(a: int, b: int) -> int:
            return a + b

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        accumulator = [[0] * cols for _ in range(rows)]
        tally = 0

        p1 = 0
        while p1 < rows:
            p2 = 0
            while p2 < cols:
                if p1 == 0 and p2 == 0:
                    accumulator[p1][p2] = grid[p1][p2]
                else:
                    if p1 == 0:
                        accumulator[p1][p2] = addValues(accumulator[p1][p2 - 1], grid[p1][p2])
                    else:
                        if p2 == 0:
                            accumulator[p1][p2] = addValues(accumulator[p1 - 1][p2], grid[p1][p2])
                        else:
                            temp1 = addValues(accumulator[p1][p2 - 1], accumulator[p1 - 1][p2])
                            temp2 = accumulator[p1 - 1][p2 - 1]
                            accumulator[p1][p2] = addValues(addValues(temp1, -temp2), grid[p1][p2])

                if accumulator[p1][p2] <= k:
                    tally += 1

                p2 += 1
            p1 += 1

        return tally