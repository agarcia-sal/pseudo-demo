from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        directions = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

        def knightReachable(cx, cy, tx, ty):
            visitedPositions = set()
            explorationQueue = deque([(cx, cy, 0)])
            visitedPositions.add((cx, cy))

            while explorationQueue:
                currentX, currentY, dist = explorationQueue.popleft()
                if currentX == tx and currentY == ty:
                    return dist
                for dx, dy in directions:
                    nextX, nextY = currentX + dx, currentY + dy
                    if 0 <= nextX < 50 and 0 <= nextY < 50:
                        candidate = (nextX, nextY)
                        if candidate not in visitedPositions:
                            visitedPositions.add(candidate)
                            explorationQueue.append((nextX, nextY, dist + 1))
            return -1

        totalPositions = len(positions)
        convertedPositions = [tuple(pos) for pos in positions]

        memo = {}

        def innerDP(cx, cy, bitmask, playerTurn):
            if bitmask == 0:
                return 0
            key = (cx, cy, bitmask, playerTurn)
            if key in memo:
                return memo[key]

            if playerTurn:
                bestScore = 0
            else:
                bestScore = float('inf')

            idx = 0
            while idx < totalPositions:
                if (bitmask & (1 << idx)) != 0:
                    tx, ty = convertedPositions[idx]
                    moveCost = knightReachable(cx, cy, tx, ty)
                    if moveCost != -1:
                        updatedMask = bitmask ^ (1 << idx)
                        nextValue = moveCost + innerDP(tx, ty, updatedMask, not playerTurn)
                        if playerTurn:
                            if bestScore < nextValue:
                                bestScore = nextValue
                        else:
                            if bestScore > nextValue:
                                bestScore = nextValue
                idx += 1

            memo[key] = bestScore
            return bestScore

        fullMask = (1 << totalPositions) - 1
        return innerDP(kx, ky, fullMask, True)