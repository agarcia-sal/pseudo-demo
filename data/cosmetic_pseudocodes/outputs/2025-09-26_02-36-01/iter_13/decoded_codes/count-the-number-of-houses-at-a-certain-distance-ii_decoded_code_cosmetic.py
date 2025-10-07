from collections import deque

class Solution:
    def countOfPairs(self, n, x, y):
        def swapIfNeeded():
            nonlocal x, y
            if x > y:
                x, y = y, x

        swapIfNeeded()

        def bfs(start):
            visitedList = [False] * (n + 1)
            distList = [0] * (n + 1)

            queueStruct = deque([start])
            visitedList[start] = True

            def processNeighbor(currentVal, neighborVal):
                if 1 <= neighborVal <= n and not visitedList[neighborVal]:
                    visitedList[neighborVal] = True
                    distList[neighborVal] = distList[currentVal] + 1
                    queueStruct.append(neighborVal)

            while queueStruct:
                currentVal = queueStruct.popleft()

                processNeighbor(currentVal, currentVal - 1)
                processNeighbor(currentVal, currentVal + 1)

                if currentVal == x:
                    if not visitedList[y]:
                        visitedList[y] = True
                        distList[y] = distList[currentVal] + 1
                        queueStruct.append(y)
                elif currentVal == y:
                    if not visitedList[x]:
                        visitedList[x] = True
                        distList[x] = distList[currentVal] + 1
                        queueStruct.append(x)

            # Equivalent of sliceList(distList, 1)
            return distList[1:]

        def forEach(collection, action):
            idx = 0
            length = len(collection)
            while idx < length:
                action(collection[idx])
                idx += 1

        finalResult = [0] * n

        def incrementAtIndex(idx):
            finalResult[idx] += 1

        outerIdx = 1
        while outerIdx <= n:
            tempDistances = bfs(outerIdx)

            def processD(value):
                if value > 0:
                    incrementAtIndex(value - 1)

            forEach(tempDistances, processD)

            outerIdx += 1

        return finalResult