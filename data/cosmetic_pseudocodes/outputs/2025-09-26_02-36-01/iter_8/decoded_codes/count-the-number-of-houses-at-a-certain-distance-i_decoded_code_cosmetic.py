from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        outcome = [0] * n

        def bfs(start: int) -> None:
            flagArray = [False] * (n + 1)
            distArray = [0] * (n + 1)
            deq = deque()

            deq.append(start)
            flagArray[start] = True

            def isValid(pos: int) -> bool:
                return 1 <= pos <= n

            while deq:
                currentPos = deq.popleft()
                adjacentNodes = [currentPos - 1, currentPos + 1]

                for neighborNode in adjacentNodes:
                    if isValid(neighborNode):
                        if not flagArray[neighborNode]:
                            flagArray[neighborNode] = True
                            distArray[neighborNode] = distArray[currentPos] + 1
                            deq.append(neighborNode)

                if currentPos == x:
                    if not flagArray[y]:
                        flagArray[y] = True
                        distArray[y] = distArray[currentPos] + 1
                        deq.append(y)

                if currentPos == y:
                    if not flagArray[x]:
                        flagArray[x] = True
                        distArray[x] = distArray[currentPos] + 1
                        deq.append(x)

            for i in range(1, n + 1):
                distanceValue = distArray[i]
                if distanceValue > 0:
                    outcome[distanceValue - 1] += 1

        for outerIter in range(1, n + 1):
            bfs(outerIter)

        return outcome