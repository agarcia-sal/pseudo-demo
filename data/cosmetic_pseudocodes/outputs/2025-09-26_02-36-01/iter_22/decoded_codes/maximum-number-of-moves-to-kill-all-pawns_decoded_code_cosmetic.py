from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx, ky, positions):
        directions = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        pawnsSet = set(tuple(pos) for pos in positions)
        positions = list(pawnsSet)
        totalPawns = len(positions)

        from functools import lru_cache

        @lru_cache(None)
        def dp(kx, ky, mask, isAlice):
            if mask == 0:
                return 0

            if isAlice:
                val = 0
            else:
                val = inf

            for idx in range(totalPawns):
                if (mask & (1 << idx)) != 0:
                    targetX, targetY = positions[idx]

                    q = deque([(kx, ky, 0)])
                    seen = {(kx, ky)}
                    foundFlag = False

                    while q:
                        curX, curY, steps = q.popleft()
                        if curX == targetX and curY == targetY:
                            foundFlag = True
                            break
                        for deltaX, deltaY in directions:
                            nxtX = curX + deltaX
                            nxtY = curY + deltaY
                            if 0 <= nxtX < 50 and 0 <= nxtY < 50 and (nxtX, nxtY) not in seen:
                                seen.add((nxtX, nxtY))
                                q.append((nxtX, nxtY, steps + 1))

                    if foundFlag:
                        newMask = mask ^ (1 << idx)
                        candidate = steps + dp(targetX, targetY, newMask, not isAlice)
                        if isAlice:
                            if val < candidate:
                                val = candidate
                        else:
                            if val > candidate:
                                val = candidate

            return val

        fullMask = (1 << totalPawns) - 1
        return dp(kx, ky, fullMask, True)