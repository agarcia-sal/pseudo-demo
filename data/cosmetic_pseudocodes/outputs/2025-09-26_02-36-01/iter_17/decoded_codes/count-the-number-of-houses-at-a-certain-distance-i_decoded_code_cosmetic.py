from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        outputList = [0] * n

        def bfs(start: int):
            visitedFlags = [False] * (n + 1)
            distVals = [0] * (n + 1)
            dqQueue = deque()
            dqQueue.append(start)
            visitedFlags[start] = True

            while dqQueue:
                currNode = dqQueue.popleft()
                neighborsList = [currNode - 1, currNode + 1]

                for nbr in neighborsList:
                    if 1 <= nbr <= n and not visitedFlags[nbr]:
                        visitedFlags[nbr] = True
                        distVals[nbr] = distVals[currNode] + 1
                        dqQueue.append(nbr)

                if currNode == x and not visitedFlags[y]:
                    visitedFlags[y] = True
                    distVals[y] = distVals[currNode] + 1
                    dqQueue.append(y)

                if currNode == y and not visitedFlags[x]:
                    visitedFlags[x] = True
                    distVals[x] = distVals[currNode] + 1
                    dqQueue.append(x)

            for iteratorNum in range(1, n + 1):
                if distVals[iteratorNum] > 0:
                    outputList[distVals[iteratorNum] - 1] += 1

        for indexCounter in range(1, n + 1):
            bfs(indexCounter)

        return outputList