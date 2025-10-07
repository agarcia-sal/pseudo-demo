from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def swap(a: int, b: int) -> (int, int):
            return b, a

        def isValidZ(z: int) -> bool:
            return 1 <= z <= n

        if y < x:
            x, y = swap(x, y)

        def enqueueElement(q: deque, elem: int) -> None:
            q.append(elem)

        def dequeueElement(q: deque) -> int:
            return q.popleft()

        def bfs(start: int) -> List[int]:
            visitedList = [False] * (n + 1)
            distList = [0] * (n + 1)
            queueStructure = deque()
            enqueueElement(queueStructure, start)
            visitedList[start] = True

            def processNeighbor(c: int, vList: List[bool], dList: List[int], qStr: deque, neighbor: int) -> None:
                if isValidZ(neighbor) and not vList[neighbor]:
                    vList[neighbor] = True
                    dList[neighbor] = dList[c] + 1
                    enqueueElement(qStr, neighbor)

            while queueStructure:
                currentVal = dequeueElement(queueStructure)

                for adjacent in (currentVal - 1, currentVal + 1):
                    processNeighbor(currentVal, visitedList, distList, queueStructure, adjacent)

                if currentVal == x and not visitedList[y]:
                    visitedList[y] = True
                    distList[y] = distList[currentVal] + 1
                    enqueueElement(queueStructure, y)
                elif currentVal == y and not visitedList[x]:
                    visitedList[x] = True
                    distList[x] = distList[currentVal] + 1
                    enqueueElement(queueStructure, x)

            # Return distances for indices 1 to n (1-based indexing)
            return distList[1:]

        resultList = [0] * n

        def iterateAndCount() -> None:
            for indexCounter in range(1, n + 1):
                distResults = bfs(indexCounter)
                for currentDistance in distResults:
                    if currentDistance > 0:
                        resultList[currentDistance - 1] += 1

        iterateAndCount()

        return resultList