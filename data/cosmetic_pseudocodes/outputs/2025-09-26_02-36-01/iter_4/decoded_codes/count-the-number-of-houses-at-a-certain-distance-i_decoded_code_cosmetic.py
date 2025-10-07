from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        outputList = [0] * n

        def bfs(start: int) -> None:
            seen = [False] * (n + 1)
            distArray = [0] * (n + 1)
            dequeContainer = deque([start])
            seen[start] = True

            while dequeContainer:
                node = dequeContainer.popleft()
                adjacents = [node - 1, node + 1]

                for neighbor in adjacents:
                    if 1 <= neighbor <= n and not seen[neighbor]:
                        seen[neighbor] = True
                        distArray[neighbor] = distArray[node] + 1
                        dequeContainer.append(neighbor)

                if node == x and not seen[y]:
                    seen[y] = True
                    distArray[y] = distArray[node] + 1
                    dequeContainer.append(y)

                if node == y and not seen[x]:
                    seen[x] = True
                    distArray[x] = distArray[node] + 1
                    dequeContainer.append(x)

            for position in range(1, n + 1):
                if distArray[position] > 0:
                    index = distArray[position] - 1
                    outputList[index] += 1

        for counter in range(1, n + 1):
            bfs(counter)

        return outputList