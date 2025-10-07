from collections import deque
from math import inf
from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knightDirs = [(+2, +1), (+1, +2), (-1, +2), (-2, +1),
                      (-2, -1), (-1, -2), (+1, -2), (+2, -1)]
        collectedPawns = set()
        idxCounter = 0
        while idxCounter < len(positions):
            currentPos = (positions[idxCounter][0], positions[idxCounter][1])
            collectedPawns.add(currentPos)
            idxCounter += 1

        totalPawns = len(collectedPawns)

        @lru_cache(None)
        def dp(qx, qy, bitmask, aliceTurn):
            if bitmask == 0:
                return 0

            if aliceTurn:
                limitVal = 0
            else:
                limitVal = inf

            for iterator in range(totalPawns):
                if bitmask & (1 << iterator):
                    targetX, targetY = positions[iterator]

                    lineQueue = deque()
                    lineQueue.append((qx, qy, 0))
                    exploredSet = set()
                    exploredSet.add((qx, qy))
                    wasFound = False

                    while lineQueue:
                        currX, currY, walkSteps = lineQueue.popleft()
                        if currX == targetX and currY == targetY:
                            wasFound = True
                            break

                        for dx, dy in knightDirs:
                            newX, newY = currX + dx, currY + dy
                            if 0 <= newX < 50 and 0 <= newY < 50 and (newX, newY) not in exploredSet:
                                exploredSet.add((newX, newY))
                                lineQueue.append((newX, newY, walkSteps + 1))

                    if wasFound:
                        newBitmask = bitmask ^ (1 << iterator)
                        tempCalc = walkSteps + dp(targetX, targetY, newBitmask, not aliceTurn)

                        if aliceTurn:
                            if tempCalc > limitVal:
                                limitVal = tempCalc
                        else:
                            if tempCalc < limitVal:
                                limitVal = tempCalc
            return limitVal

        fullMask = (1 << totalPawns) - 1
        return dp(kx, ky, fullMask, True)