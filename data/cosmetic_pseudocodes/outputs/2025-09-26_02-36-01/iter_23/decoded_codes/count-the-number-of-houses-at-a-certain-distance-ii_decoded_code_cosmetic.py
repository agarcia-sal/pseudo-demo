from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int):
        if x > y:
            x, y = y, x

        def bfs(startIndex: int):
            flagList = [False] * (n + 1)
            distList = [0] * (n + 1)
            deq = deque([startIndex])
            flagList[startIndex] = True

            def bfsLoop(queue: deque):
                while queue:
                    currNode = queue.popleft()

                    neighborSet = [currNode - 1, currNode + 1]
                    for nbrElement in neighborSet:
                        if 1 <= nbrElement <= n and not flagList[nbrElement]:
                            flagList[nbrElement] = True
                            distList[nbrElement] = distList[currNode] + 1
                            queue.append(nbrElement)

                    if currNode == x and not flagList[y]:
                        flagList[y] = True
                        distList[y] = distList[currNode] + 1
                        queue.append(y)
                    elif currNode == y and not flagList[x]:
                        flagList[x] = True
                        distList[x] = distList[currNode] + 1
                        queue.append(x)

            bfsLoop(deq)
            return distList[1:]

        countArr = [0] * n

        def outerLoop(iIndex: int):
            if iIndex > n:
                return
            distRes = bfs(iIndex)

            def innerLoop(kIndex: int):
                if kIndex > n - 1:
                    return
                valDist = distRes[kIndex]
                if valDist > 0:
                    countArr[valDist - 1] += 1
                innerLoop(kIndex + 1)

            innerLoop(0)
            outerLoop(iIndex + 1)

        outerLoop(1)
        return countArr