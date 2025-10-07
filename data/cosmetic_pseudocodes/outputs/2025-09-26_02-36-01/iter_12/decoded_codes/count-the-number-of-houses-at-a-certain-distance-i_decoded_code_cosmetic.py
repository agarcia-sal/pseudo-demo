from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:

        def enqueueHelper(dq: deque, val: int) -> None:
            dq.append(val)

        def dequeueHelper(dq: deque) -> int:
            return dq.popleft()

        def makeFalseList(size: int) -> list[bool]:
            tempList = []
            index = 0
            while True:
                if index == size:
                    break
                tempList.append(False)
                index += 1
            return tempList

        def makeZeroList(size: int) -> list[int]:
            zeros = []
            counter = 0
            while True:
                if counter == size:
                    break
                zeros.append(0)
                counter += 1
            return zeros

        output = makeZeroList(n)

        def bfs(start: int) -> None:
            visitedFlags = makeFalseList(n + 1)
            distances = makeZeroList(n + 1)
            dq = deque()
            enqueueHelper(dq, start)
            visitedFlags[start] = True

            def neighbors(currentVal: int) -> list[int]:
                return [currentVal - 1, currentVal + 1]

            while True:
                if not dq:
                    break

                node = dequeueHelper(dq)
                adjacentNodes = neighbors(node)
                idx = 0
                while True:
                    if idx >= 2:
                        break
                    neighborNode = adjacentNodes[idx]
                    if 1 <= neighborNode <= n:
                        if visitedFlags[neighborNode] is False:
                            visitedFlags[neighborNode] = True
                            distances[neighborNode] = distances[node] + 1
                            enqueueHelper(dq, neighborNode)
                    idx += 1

                if node == x:
                    if not visitedFlags[y]:
                        visitedFlags[y] = True
                        distances[y] = distances[node] + 1
                        enqueueHelper(dq, y)

                if node == y:
                    if not visitedFlags[x]:
                        visitedFlags[x] = True
                        distances[x] = distances[node] + 1
                        enqueueHelper(dq, x)

            pos = 1
            while True:
                if pos > n:
                    break
                if distances[pos] > 0:
                    outputAtIndex = distances[pos] - 1
                    output[outputAtIndex] += 1
                pos += 1

        iter = 1
        while True:
            if iter > n:
                break
            bfs(iter)
            iter += 1

        return output