from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        way = [0] * n

        def traverse(r: int) -> None:
            proto = [False] * (n + 1)
            step = [0] * (n + 1)
            hold = deque([r])
            proto[r] = True

            while hold:
                now = hold.popleft()
                for adj in (now - 1, now + 1):
                    if 1 <= adj <= n and not proto[adj]:
                        proto[adj] = True
                        step[adj] = step[now] + 1
                        hold.append(adj)

                if now == x and not proto[y]:
                    proto[y] = True
                    step[y] = step[now] + 1
                    hold.append(y)
                elif now == y and not proto[x]:
                    proto[x] = True
                    step[x] = step[now] + 1
                    hold.append(x)

            for c in range(1, n + 1):
                if step[c] > 0:
                    idx = step[c] - 1
                    way[idx] += 1

        for b in range(1, n + 1):
            traverse(b)

        return way