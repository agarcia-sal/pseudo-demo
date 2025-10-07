from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ds = len(grid)
        tq = len(grid[0])
        xv = 0

        wi = 0
        while wi < tq:
            km = 0
            while km + 1 < ds:
                if grid[km][wi] != grid[km + 1][wi]:
                    xv += 1
                    grid[km + 1][wi] = grid[km][wi]
                km += 1

            oe = 0
            while oe < ds:
                if wi < tq - 1 and grid[oe][wi] == grid[oe][wi + 1]:
                    xv += 1
                    for an in range(10):
                        if an != grid[oe][wi]:
                            grid[oe][wi + 1] = an
                            break
                oe += 1

            wi += 1

        return xv