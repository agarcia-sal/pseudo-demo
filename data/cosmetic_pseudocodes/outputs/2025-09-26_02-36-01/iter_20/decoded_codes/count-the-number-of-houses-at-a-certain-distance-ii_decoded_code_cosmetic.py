class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        def helperBFS(startNode: int) -> list[int]:
            def initializeLists(size: int, initVal):
                arr = []
                idx = 0
                while True:
                    if idx >= size:
                        break
                    arr.append(initVal)
                    idx += 1
                return arr

            visitedNodes = initializeLists(n + 1, False)
            distValues = initializeLists(n + 1, 0)

            def enqueue(queueRef: list[int], value: int):
                queueRef.append(value)

            q = []
            enqueue(q, startNode)
            visitedNodes[startNode] = True

            def dequeue(queueRef: list[int]) -> int:
                firstElem = queueRef[0]
                del queueRef[0]
                return firstElem

            def processNeighbor(neighb: int, curr: int):
                if 1 <= neighb <= n and visitedNodes[neighb] is False:
                    visitedNodes[neighb] = True
                    distValues[neighb] = distValues[curr] + 1
                    enqueue(q, neighb)

            while True:
                if len(q) == 0:
                    break
                currNode = dequeue(q)

                neighborsList = [currNode - 1, currNode + 1]
                for nb in neighborsList:
                    processNeighbor(nb, currNode)

                if currNode == x and visitedNodes[y] is False:
                    visitedNodes[y] = True
                    distValues[y] = distValues[currNode] + 1
                    enqueue(q, y)
                else:
                    if currNode == y and visitedNodes[x] is False:
                        visitedNodes[x] = True
                        distValues[x] = distValues[currNode] + 1
                        enqueue(q, x)

            def sliceList(fullList: list[int], startIndex: int) -> list[int]:
                sliced = []
                idx2 = startIndex
                while True:
                    if idx2 > len(fullList):
                        break
                    if idx2 == len(fullList):
                        break
                    sliced.append(fullList[idx2])
                    idx2 += 1
                return sliced

            return sliceList(distValues, 1)

        def swapIfGT(refA: int, refB: int):
            if refA > refB:
                return refB, refA
            return refA, refB

        x, y = swapIfGT(x, y)

        resultsList = []
        iCounter = 1
        while True:
            if iCounter > n:
                break
            distList = helperBFS(iCounter)
            for distItem in distList:
                if distItem > 0:
                    while len(resultsList) < distItem:
                        resultsList.append(0)
                    resultsList[distItem - 1] += 1
            iCounter += 1

        return resultsList