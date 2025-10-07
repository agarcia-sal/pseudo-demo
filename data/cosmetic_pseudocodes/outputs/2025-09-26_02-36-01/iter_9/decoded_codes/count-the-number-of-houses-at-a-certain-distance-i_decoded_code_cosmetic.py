from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        outputList = [0] * n

        def traverseGraph(origin: int) -> None:
            def addToQueueIfValid(idx: int, queueRef: deque, visitedRef: List[bool], distRef: List[int]) -> None:
                if 1 <= idx <= n and not visitedRef[idx]:
                    visitedRef[idx] = True
                    distRef[idx] = distRef[originPtr] + 1
                    queueRef.append(idx)

            visitedNodes = [False] * (n + 1)
            nodeDistance = [0] * (n + 1)
            originPtr = origin
            visitedNodes[originPtr] = True
            frontier = deque([originPtr])

            while frontier:
                currentNode = frontier.popleft()

                addToQueueIfValid(currentNode - 1, frontier, visitedNodes, nodeDistance)
                addToQueueIfValid(currentNode + 1, frontier, visitedNodes, nodeDistance)

                if currentNode == x and not visitedNodes[y]:
                    visitedNodes[y] = True
                    nodeDistance[y] = nodeDistance[currentNode] + 1
                    frontier.append(y)

                if currentNode == y and not visitedNodes[x]:
                    visitedNodes[x] = True
                    nodeDistance[x] = nodeDistance[currentNode] + 1
                    frontier.append(x)

            for idx in range(1, n + 1):
                if nodeDistance[idx] > 0:
                    outputList[nodeDistance[idx] - 1] += 1

        for counter in range(1, n + 1):
            traverseGraph(counter)

        return outputList