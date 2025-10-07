from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx, ky, positions):
        c0 = 2
        knight_moves = [
            (c0 - 2, c0 - 1), (c0 - 2, c0 + 1), (c0 - 1, c0 + 2), (c0 + 1, c0 + 2),
            (c0 + 2, c0 + 1), (c0 + 2, c0 - 1), (c0 + 1, c0 - 2), (c0 - 1, c0 - 2)
        ]
        # Adjust knight_moves to relative differences around zero
        # (c0=2) gives moves: (0,1),(0,3),(1,4),(3,4),(4,3),(4,1),(3,0),(1,0) which is invalid;
        # It must represent standard knight moves around current (cx,cy):
        # So adjust to the original expected relative moves:
        knight_moves = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2),
            (2, 1), (2, -1), (1, -2), (-1, -2)
        ]

        pawnsSet = set((x, y) for x, y in positions)
        pLen = len(positions)

        def bfs(startX, startY, targetX, targetY):
            if (startX, startY) == (targetX, targetY):
                return True, 0
            openList = deque([(startX, startY, 0)])
            marked = {(startX, startY)}

            def exploreNeighbours(cx, cy):
                if cx < 0 or cx >= 50 or cy < 0 or cy >= 50:
                    return []
                neighbors = []
                for dx, dy in knight_moves:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in marked:
                        neighbors.append((nx, ny))
                return neighbors

            while openList:
                currX, currY, currDist = openList.popleft()
                if currX == targetX and currY == targetY:
                    return True, currDist
                adjacent = exploreNeighbours(currX, currY)
                for adjX, adjY in adjacent:
                    marked.add((adjX, adjY))
                    openList.append((adjX, adjY, currDist + 1))
            return False, 0

        memo = {}

        def toggleBool(b):
            return not b

        def dp(xA, yA, m0, aliceTurn):
            if m0 == 0:
                return 0
            key = (xA, yA, m0, aliceTurn)
            if key in memo:
                return memo[key]

            metric = 0 if aliceTurn else inf

            for idx0 in range(pLen):
                bitFlag = 1 << idx0
                if (m0 & bitFlag) != 0:
                    px, py = positions[idx0]
                    reachable, distVal = bfs(xA, yA, px, py)
                    if reachable:
                        updatedMask = m0 ^ bitFlag
                        tempVal = distVal + dp(px, py, updatedMask, toggleBool(aliceTurn))
                        if aliceTurn:
                            if tempVal > metric:
                                metric = tempVal
                        else:
                            if tempVal < metric:
                                metric = tempVal

            memo[key] = metric
            return metric

        fullMask = (1 << pLen) - 1
        return dp(kx, ky, fullMask, True)