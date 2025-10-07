class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        def helperIsQueueEmpty(q: list) -> bool:
            return len(q) == 0

        outputList = [0] * n

        def bfs(start: int):
            seenList = [False] * (n + 1)
            distList = [0] * (n + 1)
            workQueue = []

            workQueue.append(start)
            seenList[start] = True

            while True:
                if helperIsQueueEmpty(workQueue):
                    break
                currentNode = workQueue.pop(0)
                neighborCandidates = [currentNode - 1, currentNode + 1]

                for neighborVal in neighborCandidates:
                    if 1 <= neighborVal <= n and not seenList[neighborVal]:
                        seenList[neighborVal] = True
                        distList[neighborVal] = distList[currentNode] + 1
                        workQueue.append(neighborVal)

                if currentNode == x:
                    if not seenList[y]:
                        seenList[y] = True
                        distList[y] = distList[currentNode] + 1
                        workQueue.append(y)
                if currentNode == y:
                    if not seenList[x]:
                        seenList[x] = True
                        distList[x] = distList[currentNode] + 1
                        workQueue.append(x)

            distVal = 1
            while distVal <= n:
                if distList[distVal] != 0:
                    zeroIndex = distList[distVal] - 1
                    outputList[zeroIndex] += 1
                distVal += 1

        loopVar = 1
        while True:
            if loopVar > n:
                break
            bfs(loopVar)
            loopVar += 1

        return outputList