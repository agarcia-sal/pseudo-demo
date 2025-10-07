from collections import deque
from math import inf

class Solution:
    def maxMoves(self, x_1, y_1, pos_list):
        knightDirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        pawns_set = {(x, y) for x, y in pos_list}
        total_pawns = len(pawns_set)
        pawns = list(pawns_set)  # to get consistent indexing

        from functools import lru_cache

        @lru_cache(None)
        def recurse(a_x, a_y, stateMask, aliceTurn):
            if stateMask == 0:
                return 0

            if aliceTurn:
                resultVal = 0
            else:
                resultVal = inf

            for idx in range(total_pawns):
                if (stateMask & (1 << idx)) != 0:
                    targetX, targetY = pawns[idx]

                    toVisitQueue = deque([(a_x, a_y, 0)])
                    discovered = {(a_x, a_y)}
                    foundFlag = False
                    dist = 0

                    while toVisitQueue:
                        curX, curY, dist = toVisitQueue.popleft()

                        if curX == targetX and curY == targetY:
                            foundFlag = True
                            break

                        for dx, dy in knightDirs:
                            nx, ny = curX + dx, curY + dy
                            if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in discovered:
                                discovered.add((nx, ny))
                                toVisitQueue.append((nx, ny, dist + 1))

                    if foundFlag:
                        nextMask = stateMask ^ (1 << idx)
                        alternative = dist + recurse(targetX, targetY, nextMask, not aliceTurn)

                        if aliceTurn:
                            if resultVal < alternative:
                                resultVal = alternative
                        else:
                            if resultVal > alternative:
                                resultVal = alternative

            return resultVal

        fullMask = (1 << total_pawns) - 1
        return recurse(x_1, y_1, fullMask, True)