from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(origin: int) -> list[int]:
            visitedFlags = [False] * (n + 1)
            distSteps = [0] * (n + 1)
            processingQueue = deque([origin])
            visitedFlags[origin] = True

            while processingQueue:
                currentNode = processingQueue.popleft()
                neighborsList = [currentNode - 1, currentNode + 1]

                for adjacentNode in neighborsList:
                    if 1 <= adjacentNode <= n and not visitedFlags[adjacentNode]:
                        visitedFlags[adjacentNode] = True
                        distSteps[adjacentNode] = distSteps[currentNode] + 1
                        processingQueue.append(adjacentNode)

                if currentNode == x and not visitedFlags[y]:
                    visitedFlags[y] = True
                    distSteps[y] = distSteps[currentNode] + 1
                    processingQueue.append(y)
                elif currentNode == y and not visitedFlags[x]:
                    visitedFlags[x] = True
                    distSteps[x] = distSteps[currentNode] + 1
                    processingQueue.append(x)

            return distSteps[1:]

        countArray = [0] * n
        counterIndex = 1
        while counterIndex <= n:
            bfsDistances = bfs(counterIndex)
            for distValue in bfsDistances:
                if distValue != 0:
                    countArray[distValue - 1] += 1
            counterIndex += 1

        return countArray