from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knightDirections = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        pawnsSet = set()

        def fillPawnsSet(posList, idx, limit):
            if idx == limit:
                return
            currentPos = (posList[idx][0], posList[idx][1])
            pawnsSet.add(currentPos)
            fillPawnsSet(posList, idx + 1, limit)

        fillPawnsSet(positions, 0, len(positions))
        countPawns = len(pawnsSet)

        # Convert pawnsSet to a fixed list to keep positions order consistent
        # positions input may have duplicates; pawnsSet removes duplicates.
        # dp references by index, so order matters:
        # We'll re-order positions to only those in pawnsSet preserving order from original positions,
        # but skipping duplicates.
        positions_filtered = []
        seen = set()
        for p in positions:
            pt = (p[0], p[1])
            if pt in pawnsSet and pt not in seen:
                positions_filtered.append(pt)
                seen.add(pt)

        # Create a mapping from index to position for dp
        positions = positions_filtered

        @lru_cache(None)
        def dp(kxP, kyP, bitmask, aliceTurn):
            if bitmask == 0:
                return 0

            if aliceTurn:
                bestValue = 0
            else:
                bestValue = float('inf')

            def loopIndices(indx, boundary, currentBest):
                if indx >= boundary:
                    return currentBest

                bitTest = 1 << indx
                if (bitmask & bitTest) != 0:
                    targetX, targetY = positions[indx]

                    bfsQueue = [(kxP, kyP, 0)]
                    visitedNodes = {(kxP, kyP)}

                    def bfsProcess(queue):
                        if len(queue) == 0:
                            return -1

                        cx, cy, stepCount = queue[0]
                        restQueue = queue[1:]

                        if cx == targetX and cy == targetY:
                            return stepCount

                        newQueue = restQueue

                        def processDirections(dirs, idxDir, limitDir, qAcc):
                            if idxDir >= limitDir:
                                return qAcc
                            dx, dy = dirs[idxDir]
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visitedNodes:
                                visitedNodes.add((nx, ny))
                                qAcc.append((nx, ny, stepCount + 1))
                            return processDirections(dirs, idxDir + 1, limitDir, qAcc)

                        updatedQueue = processDirections(knightDirections, 0, len(knightDirections), newQueue)
                        return bfsProcess(updatedQueue)

                    distSteps = bfsProcess(bfsQueue)
                    if distSteps != -1:
                        newMask = bitmask ^ (1 << indx)
                        recursiveCall = dp(targetX, targetY, newMask, not aliceTurn)
                        combinedSteps = distSteps + recursiveCall
                        if aliceTurn:
                            if currentBest < combinedSteps:
                                currentBest = combinedSteps
                        else:
                            if currentBest > combinedSteps:
                                currentBest = combinedSteps
                    return loopIndices(indx + 1, boundary, currentBest)
                else:
                    return loopIndices(indx + 1, boundary, currentBest)

            bestValue = loopIndices(0, countPawns, bestValue)
            return bestValue

        fullMask = (1 << countPawns) - 1
        finalAnswer = dp(kx, ky, fullMask, True)
        return finalAnswer