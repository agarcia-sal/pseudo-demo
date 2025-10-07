from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[Tuple[int, int]], edges2: List[Tuple[int, int]]) -> List[int]:
        neighborsA = defaultdict(list)
        neighborsB = defaultdict(list)

        for x, y in edges1:
            neighborsA[x].append(y)
            neighborsA[y].append(x)

        for p, q in edges2:
            neighborsB[p].append(q)
            neighborsB[q].append(p)

        sizeA = len(neighborsA)
        sizeB = len(neighborsB)

        def traverseBreadth(graph: defaultdict, origin: int) -> Tuple[int, int]:
            countEven = 0
            countOdd = 0
            waitingList = deque([(origin, 0)])
            visitedNodes = {origin}

            while waitingList:
                currentNode, depth = waitingList.popleft()

                if depth % 2 == 0:
                    countEven += 1
                else:
                    countOdd += 1

                for adjacentNode in graph[currentNode]:
                    if adjacentNode not in visitedNodes:
                        visitedNodes.add(adjacentNode)
                        waitingList.append((adjacentNode, depth + 1))

            return countEven, countOdd

        recordA = []
        for indexA in range(sizeA):
            recordA.append(traverseBreadth(neighborsA, indexA))

        recordB = []
        for indexB in range(sizeB):
            recordB.append(traverseBreadth(neighborsB, indexB))

        finalResult = []
        for outerIndex in range(sizeA):
            evensA, oddsA = recordA[outerIndex]
            localMax = 0

            for innerIndex in range(sizeB):
                evensB, oddsB = recordB[innerIndex]
                if outerIndex == innerIndex or (outerIndex % 2) == (innerIndex % 2):
                    candidate = evensB
                else:
                    candidate = oddsB

                if candidate > localMax:
                    localMax = candidate

            finalResult.append(evensA + localMax)

        return finalResult