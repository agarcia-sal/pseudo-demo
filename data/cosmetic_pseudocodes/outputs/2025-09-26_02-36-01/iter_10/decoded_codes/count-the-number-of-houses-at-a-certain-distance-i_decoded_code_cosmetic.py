from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:

        def enqueue_if_valid(z: int, visitedRef: list[bool], distanceRef: list[int], queueRef: deque[int], currentRef: int) -> None:
            if 1 <= z <= n and not visitedRef[z]:
                visitedRef[z] = True
                distanceRef[z] = distanceRef[currentRef] + 1
                queueRef.append(z)

        def breadthFirstSearch(start: int) -> None:
            markedList = [False] * (n + 1)
            distList = [0] * (n + 1)
            queue = deque()

            queue.append(start)
            markedList[start] = True

            def loopProcess() -> None:
                if not queue:
                    return

                currentNode = queue.popleft()

                enqueue_if_valid(currentNode - 1, markedList, distList, queue, currentNode)
                enqueue_if_valid(currentNode + 1, markedList, distList, queue, currentNode)

                if currentNode == x and not markedList[y]:
                    markedList[y] = True
                    distList[y] = distList[currentNode] + 1
                    queue.append(y)

                if currentNode == y and not markedList[x]:
                    markedList[x] = True
                    distList[x] = distList[currentNode] + 1
                    queue.append(x)

                loopProcess()

            loopProcess()

            for distVal in range(1, n + 1):
                d = distList[distVal]
                if d > 0:
                    result[d - 1] += 1

        result = [0] * n
        outerCounter = 1
        while outerCounter <= n:
            breadthFirstSearch(outerCounter)
            outerCounter += 1

        return result