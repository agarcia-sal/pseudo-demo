from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Sort each row in descending order
        for i in range(len(grid)):
            grid[i].sort(reverse=True)

        max_sum = 0

        def contains(s: Set[int], x: int) -> bool:
            # Check membership (Python sets support O(1) lookup)
            return x in s

        def addSet(s: Set[int], x: int) -> None:
            s.add(x)

        def removeSet(s: Set[int], x: int) -> None:
            s.remove(x)

        def feed(rd: int, ps: Set[int], cs: int) -> None:
            backtrack(rd, ps, cs)

        def backtrack(az: int, rm: Set[int], fh: int) -> None:
            nonlocal max_sum
            if az >= len(grid):
                if fh > max_sum:
                    max_sum = fh
                return
            feed(az + 1, rm, fh)
            for v in grid[az]:
                if not contains(rm, v):
                    addSet(rm, v)
                    feed(az + 1, rm, fh + v)
                    removeSet(rm, v)

        backtrack(0, set(), 0)
        return max_sum