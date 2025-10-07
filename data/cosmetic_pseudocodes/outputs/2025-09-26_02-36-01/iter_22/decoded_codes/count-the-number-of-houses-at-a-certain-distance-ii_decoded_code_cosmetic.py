from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        swapped = False
        if y < x:
            x, y = y, x
            swapped = True

        def bfs(start: int) -> List[int]:
            visitedFlags = [False] * (n + 1)
            distancesArray = [0] * (n + 1)
            fifoQueue = deque([start])
            visitedFlags[start] = True

            while fifoQueue:
                currNode = fifoQueue.popleft()

                for adjacent in (currNode - 1, currNode + 1):
                    if 1 <= adjacent <= n and not visitedFlags[adjacent]:
                        visitedFlags[adjacent] = True
                        distancesArray[adjacent] = distancesArray[currNode] + 1
                        fifoQueue.append(adjacent)

                if currNode == x and not visitedFlags[y]:
                    visitedFlags[y] = True
                    distancesArray[y] = distancesArray[currNode] + 1
                    fifoQueue.append(y)
                elif currNode == y and not visitedFlags[x]:
                    visitedFlags[x] = True
                    distancesArray[x] = distancesArray[currNode] + 1
                    fifoQueue.append(x)

            return distancesArray[1:]  # Skip index 0 to return 1-based results

        outputArray = [0] * n

        for counterIdx in range(1, n + 1):
            distancesList = bfs(counterIdx)
            for dist in distancesList:
                if dist > 0:
                    outputArray[dist - 1] += 1

        return outputArray