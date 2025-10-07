from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        answer = [0] * n

        def traverseBreadth(start: int) -> None:
            visitedFlags = [False] * (n + 1)
            levels = [0] * (n + 1)
            nodesQueue = deque([start])
            visitedFlags[start] = True

            while nodesQueue:
                currentNode = nodesQueue.popleft()

                for adjNode in (currentNode - 1, currentNode + 1):
                    if 1 <= adjNode <= n and not visitedFlags[adjNode]:
                        visitedFlags[adjNode] = True
                        levels[adjNode] = levels[currentNode] + 1
                        nodesQueue.append(adjNode)

                if currentNode == x and not visitedFlags[y]:
                    visitedFlags[y] = True
                    levels[y] = levels[currentNode] + 1
                    nodesQueue.append(y)

                if currentNode == y and not visitedFlags[x]:
                    visitedFlags[x] = True
                    levels[x] = levels[currentNode] + 1
                    nodesQueue.append(x)

            for idx in range(1, n + 1):
                if levels[idx] > 0:
                    answer[levels[idx] - 1] += 1

        def runTraversal() -> None:
            for counter in range(1, n + 1):
                traverseBreadth(counter)

        runTraversal()
        return answer