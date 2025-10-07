from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * (n - 1)

        def searchTraversal(root: int) -> None:
            flagged = [False] * (n + 1)
            steps = [0] * (n + 1)
            line = deque([root])
            flagged[root] = True

            while line:
                cursor = line.popleft()

                for candidate in (cursor - 1, cursor + 1):
                    if 1 <= candidate <= n and not flagged[candidate]:
                        flagged[candidate] = True
                        steps[candidate] = steps[cursor] + 1
                        line.append(candidate)

                if cursor == x and not flagged[y]:
                    flagged[y] = True
                    steps[y] = steps[cursor] + 1
                    line.append(y)

                if cursor == y and not flagged[x]:
                    flagged[x] = True
                    steps[x] = steps[cursor] + 1
                    line.append(x)

            for idx in range(1, n + 1):
                if steps[idx] > 0:
                    result[steps[idx] - 1] += 1

        for alpha in range(1, n + 1):
            searchTraversal(alpha)

        return result