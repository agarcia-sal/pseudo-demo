class Solution:
    def maxMoves(self, kx, ky, positions):
        def generateKnightSteps():
            return [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        def isValid(x, y):
            return 0 <= x < 50 and 0 <= y < 50

        def enqueue(q, item):
            q.append(item)

        def dequeue(q):
            item = q[0]
            q.pop(0)
            return item

        knights = generateKnightSteps()
        pawnsSet = set()
        for pos in positions:
            pawnsSet.add((pos[0], pos[1]))

        positions = list(pawnsSet)
        countPawns = len(pawnsSet)

        from functools import lru_cache

        @lru_cache(None)
        def dp(a, b, mask, turn):
            if mask == 0:
                return 0

            if turn:
                optimum = 0
            else:
                optimum = 10**9

            for idx in range(countPawns):
                if (mask & (1 << idx)) != 0:
                    targetX, targetY = positions[idx]

                    q = [(a, b, 0)]
                    visitedCoords = set()
                    visitedCoords.add((a, b))

                    reached = False

                    while q:
                        cx, cy, stepCount = dequeue(q)
                        if (cx, cy) == (targetX, targetY):
                            reached = True
                            break
                        for dx, dy in knights:
                            nx, ny = cx + dx, cy + dy
                            if isValid(nx, ny) and (nx, ny) not in visitedCoords:
                                visitedCoords.add((nx, ny))
                                enqueue(q, (nx, ny, stepCount + 1))

                    if reached:
                        newMask = mask ^ (1 << idx)
                        recCall = dp(targetX, targetY, newMask, not turn)
                        totalSteps = stepCount + recCall
                        if turn:
                            if optimum < totalSteps:
                                optimum = totalSteps
                        else:
                            if optimum > totalSteps:
                                optimum = totalSteps

            return optimum

        initialMask = (1 << countPawns) - 1
        return dp(kx, ky, initialMask, True)