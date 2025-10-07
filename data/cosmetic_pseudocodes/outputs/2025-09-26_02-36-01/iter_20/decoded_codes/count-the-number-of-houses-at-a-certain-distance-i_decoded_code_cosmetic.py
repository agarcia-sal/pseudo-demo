from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        oup = [0] * n

        def bfs(start: int) -> None:
            seen = [False] * (n + 1)
            dist = [0] * (n + 1)
            line = deque([start])
            seen[start] = True

            while line:
                node = line.popleft()

                adjacents = [node - 1, node + 1]

                for nbr in adjacents:
                    if 1 <= nbr <= n and not seen[nbr]:
                        seen[nbr] = True
                        dist[nbr] = dist[node] + 1
                        line.append(nbr)

                if node == x and not seen[y]:
                    seen[y] = True
                    dist[y] = dist[node] + 1
                    line.append(y)

                if node == y and not seen[x]:
                    seen[x] = True
                    dist[x] = dist[node] + 1
                    line.append(x)

            for position in range(1, n + 1):
                if dist[position] > 0:
                    idxPos = dist[position] - 1
                    oup[idxPos] += 1

        cam = 1
        while cam <= n:
            bfs(cam)
            cam += 1

        return oup