from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        prevPick = [0] * (n + 1)
        prevSkip = [0] * (n + 1)

        def fillPrefix(r: int, c: int) -> None:
            if r > n - 1:
                return
            if c > n - 1:
                fillPrefix(r + 1, 0)
                return
            prefix[c][r + 1] = prefix[c][r] + grid[r][c]
            fillPrefix(r, c + 1)
        fillPrefix(0, 0)

        def evalRow(j: int) -> None:
            if j > n - 1:
                return
            currPick = [0] * (n + 1)
            currSkip = [0] * (n + 1)

            def innerCurr(curr: int) -> None:
                if curr > n:
                    return

                def innerPrev(prev: int) -> None:
                    if prev > n:
                        return
                    if curr > prev:
                        score = prefix[j][curr - 1] - prefix[j][prev]
                        if currPick[curr] < prevSkip[prev] + score:
                            currPick[curr] = prevSkip[prev] + score
                        if currSkip[curr] < prevSkip[prev] + score:
                            currSkip[curr] = prevSkip[prev] + score
                    else:
                        score = prefix[j][prev] - prefix[j][curr]
                        if currPick[curr] < prevPick[prev] + score:
                            currPick[curr] = prevPick[prev] + score
                        if currSkip[curr] < prevPick[prev]:
                            currSkip[curr] = prevPick[prev]
                    innerPrev(prev + 1)

                innerPrev(0)
                innerCurr(curr + 1)

            innerCurr(0)

            nonlocal prevPick, prevSkip
            prevPick = currPick
            prevSkip = currSkip
            evalRow(j + 1)

        evalRow(1)

        maxVal = prevPick[0]

        def findMax(idx: int) -> None:
            nonlocal maxVal
            if idx > n:
                return
            if prevPick[idx] > maxVal:
                maxVal = prevPick[idx]
            findMax(idx + 1)
        findMax(1)

        return maxVal