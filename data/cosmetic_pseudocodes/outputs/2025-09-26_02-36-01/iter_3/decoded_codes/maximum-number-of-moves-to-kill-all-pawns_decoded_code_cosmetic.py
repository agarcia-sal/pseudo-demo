from collections import deque
from math import inf
from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knightSteps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        pawnsSet = set()
        i = 0
        while i < len(positions):
            posTuple = (positions[i][0], positions[i][1])
            pawnsSet.add(posTuple)
            i += 1
        positions = list(pawnsSet)
        totalPawns = len(pawnsSet)

        @lru_cache(None)
        def dp(x, y, mask, isAlice):
            if mask == 0:
                return 0
            maxMinVal = 0 if isAlice else inf

            for idx in range(totalPawns):
                bitMask = 1 << idx
                if (mask & bitMask) != 0:
                    pawnX, pawnY = positions[idx]
                    bfsQueue = deque()
                    bfsQueue.append((x, y, 0))
                    visitedCells = set()
                    visitedCells.add((x, y))
                    reached = False
                    currSteps = 0

                    while bfsQueue and not reached:
                        currX, currY, currSteps = bfsQueue.popleft()
                        if currX == pawnX and currY == pawnY:
                            reached = True
                            break
                        for stepX, stepY in knightSteps:
                            nextX = currX + stepX
                            nextY = currY + stepY
                            if 0 <= nextX < 50 and 0 <= nextY < 50:
                                if (nextX, nextY) not in visitedCells:
                                    visitedCells.add((nextX, nextY))
                                    bfsQueue.append((nextX, nextY, currSteps + 1))
                    if reached:
                        updatedMask = mask ^ bitMask
                        candidateVal = currSteps + dp(pawnX, pawnY, updatedMask, not isAlice)
                        if isAlice:
                            if candidateVal > maxMinVal:
                                maxMinVal = candidateVal
                        else:
                            if candidateVal < maxMinVal:
                                maxMinVal = candidateVal
            return maxMinVal

        fullMask = (1 << totalPawns) - 1
        return dp(kx, ky, fullMask, True)