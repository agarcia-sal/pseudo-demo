from collections import deque
from math import inf

class Solution:
    def maxMoves(self, killingX, killingY, posList):
        knightSteps = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
        pawnSet = set((pos[0], pos[1]) for pos in posList)
        totalPawns = len(pawnSet)

        posList = list(pawnSet)  # Deduplicate and fix indexing order for dp

        from functools import lru_cache

        @lru_cache(None)
        def dp(xr, yr, bitMask, aliceTurn):
            if bitMask == 0:
                return 0

            bestScore = 0 if aliceTurn else inf

            for idxIter in range(totalPawns):
                if (bitMask & (1 << idxIter)) != 0:
                    targetX, targetY = posList[idxIter]

                    # BFS for shortest knight distance from (xr, yr) to (targetX, targetY)
                    bfsQueue = deque()
                    bfsQueue.append((xr, yr, 0))
                    seen = set()
                    seen.add((xr, yr))
                    reached = False
                    dist = -1

                    while bfsQueue:
                        currX, currY, distCurr = bfsQueue.popleft()
                        if (currX, currY) == (targetX, targetY):
                            reached = True
                            dist = distCurr
                            break
                        for dx, dy in knightSteps:
                            nx, ny = currX + dx, currY + dy
                            if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                bfsQueue.append((nx, ny, distCurr + 1))

                    if reached:
                        nextMask = bitMask ^ (1 << idxIter)
                        nextScore = dist + dp(targetX, targetY, nextMask, not aliceTurn)
                        if aliceTurn:
                            if bestScore < nextScore:
                                bestScore = nextScore
                        else:
                            if bestScore > nextScore:
                                bestScore = nextScore
            return bestScore

        fullMask = (1 << totalPawns) - 1
        return dp(killingX, killingY, fullMask, True)