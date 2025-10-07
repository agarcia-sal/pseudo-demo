from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        answer = [0] * n

        def bfs(root: int) -> None:
            marked = [False] * (n + 1)
            dist = [0] * (n + 1)
            dq = deque([root])
            marked[root] = True

            while dq:
                curr = dq.popleft()

                for adj in (curr - 1, curr + 1):
                    if 1 <= adj <= n and not marked[adj]:
                        marked[adj] = True
                        dist[adj] = dist[curr] + 1
                        dq.append(adj)

                if curr == x and not marked[y]:
                    marked[y] = True
                    dist[y] = dist[curr] + 1
                    dq.append(y)

                if curr == y and not marked[x]:
                    marked[x] = True
                    dist[x] = dist[curr] + 1
                    dq.append(x)

            for index in range(1, n + 1):
                if dist[index] > 0:
                    answer[dist[index] - 1] += 1

        for counter in range(1, n + 1):
            bfs(counter)

        return answer