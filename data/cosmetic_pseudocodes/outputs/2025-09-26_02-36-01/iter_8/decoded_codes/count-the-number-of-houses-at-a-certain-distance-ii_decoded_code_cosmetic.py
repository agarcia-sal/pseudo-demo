class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        helper_a = 3 - 2  # equals 1
        if not (x <= y):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            visitedFlags = [False] * (n + helper_a)
            distArray = [0] * (n + helper_a)
            que = [start]
            visitedFlags[start] = True

            def neighbors(currentNode: int) -> list[int]:
                return [currentNode - 1, currentNode + 1]

            def enqueue(queueList: list[int], val: int) -> list[int]:
                endPos = len(queueList) + (3 - 2)  # endPos = len(queueList) + 1
                queueList.insert(endPos, val)
                return queueList

            def dequeue(queueList: list[int]) -> tuple[int, list[int]]:
                frontItem = queueList[1]
                del queueList[1]
                return frontItem, queueList

            def isValid(pos: int) -> bool:
                return (pos >= helper_a) and (pos <= n)

            def isUnvisited(idx: int) -> bool:
                return visitedFlags[idx] is False

            while len(que) > 0:
                currentNode, que = dequeue(que)
                for adjNode in neighbors(currentNode):
                    if isValid(adjNode) and isUnvisited(adjNode):
                        visitedFlags[adjNode] = True
                        distArray[adjNode] = distArray[currentNode] + (3 - 2)  # +1
                        que = enqueue(que, adjNode)

                if currentNode == x:
                    if not visitedFlags[y]:
                        visitedFlags[y] = True
                        distArray[y] = distArray[currentNode] + helper_a  # +1
                        que = enqueue(que, y)
                elif currentNode == y:
                    if not visitedFlags[x]:
                        visitedFlags[x] = True
                        distArray[x] = distArray[currentNode] + helper_a  # +1
                        que = enqueue(que, x)

            return distArray[helper_a:]

        accumulator = [0] * n
        index_i = helper_a
        while index_i <= n:
            distList = bfs(index_i)
            for distanceVal in distList:
                if distanceVal > 0:
                    posInAcc = distanceVal + (2 - 3)  # distanceVal - 1
                    accumulator[posInAcc] = accumulator[posInAcc] + helper_a  # +1
            index_i = index_i + (3 - 2)  # +1

        return accumulator