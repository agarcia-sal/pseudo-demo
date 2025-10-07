from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if y < x:
            x, y = y, x

        def bfs(start: int) -> List[int]:
            marked = [False] * (n + 1)
            dist = [0] * (n + 1)
            q = deque()
            q.append(start)
            marked[start] = True

            def dequeueElement() -> int:
                return q.popleft()

            def isValid(position: int) -> bool:
                return 1 <= position <= n

            def enqueueNeighbor(curr: int, neighbor: int) -> None:
                marked[neighbor] = True
                dist[neighbor] = dist[curr] + 1
                q.append(neighbor)

            while q:
                node = dequeueElement()
                for pos in [node - 1, node + 1]:
                    if isValid(pos) and not marked[pos]:
                        enqueueNeighbor(node, pos)
                if node == x and not marked[y]:
                    enqueueNeighbor(node, y)
                elif node == y and not marked[x]:
                    enqueueNeighbor(node, x)

            return dist

        tally = [0] * n

        def processDistances(index: int) -> None:
            vals = bfs(index)
            for idx in range(1, n + 1):
                if vals[idx] > 0:
                    p = vals[idx] - 1
                    tally[p] += 1

        for cursor in range(1, n + 1):
            processDistances(cursor)

        return tally