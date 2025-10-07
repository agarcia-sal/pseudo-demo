from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        knightOffsets = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
        pawnsSet = set()
        idx = 0
        while idx < len(positions):
            elem = positions[idx]
            pawnsSet.add((elem[0], elem[1]))
            idx += 1
        pawnsCount = len(pawnsSet)
        positions = list(pawnsSet)  # Now positions is the unique list of pawns' positions

        from functools import lru_cache

        @lru_cache(None)
        def dp(cx, cy, bitmask, aliceTurn):
            if bitmask == 0:
                return 0

            optScore = 0 if aliceTurn else float('inf')

            for idx in range(pawnsCount):
                if bitmask & (1 << idx):
                    targetX, targetY = positions[idx]

                    q = deque()
                    q.append((cx, cy, 0))
                    visitedCoords = {(cx, cy)}
                    foundFlag = False

                    while q:
                        curX, curY, curSteps = q.popleft()
                        if curX == targetX and curY == targetY:
                            foundFlag = True
                            break
                        for offX, offY in knightOffsets:
                            newX, newY = curX + offX, curY + offY
                            if 0 <= newX < 50 and 0 <= newY < 50:
                                if (newX, newY) not in visitedCoords:
                                    visitedCoords.add((newX, newY))
                                    q.append((newX, newY, curSteps + 1))

                    if foundFlag:
                        nextMask = bitmask ^ (1 << idx)
                        nestedVal = dp(targetX, targetY, nextMask, not aliceTurn)
                        combinedVal = curSteps + nestedVal

                        if aliceTurn:
                            if optScore < combinedVal:
                                optScore = combinedVal
                        else:
                            if optScore > combinedVal:
                                optScore = combinedVal

            return optScore

        fullMask = (1 << pawnsCount) - 1
        return dp(kx, ky, fullMask, True)