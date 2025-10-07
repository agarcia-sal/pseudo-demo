from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        __Alpha = [0] * n

        def bfs(start: int) -> None:
            __Beta = [False] * (n + 1)
            __Gamma = [0] * (n + 1)
            __Delta = deque([start])

            while True:
                if not __Delta:
                    break
                __Epsilon = __Delta.popleft()

                for __Zeta in [__Epsilon - 1, __Epsilon + 1]:
                    if 1 <= __Zeta <= n and not __Beta[__Zeta]:
                        __Beta[__Zeta] = True
                        __Gamma[__Zeta] = __Gamma[__Epsilon] + 1
                        __Delta.append(__Zeta)

                if __Epsilon == x and not __Beta[y]:
                    __Beta[y] = True
                    __Gamma[y] = __Gamma[__Epsilon] + 1
                    __Delta.append(y)

                if __Epsilon == y and not __Beta[x]:
                    __Beta[x] = True
                    __Gamma[x] = __Gamma[__Epsilon] + 1
                    __Delta.append(x)

            for __Eta in range(1, n + 1):
                if __Gamma[__Eta] > 0:
                    __Alpha[__Gamma[__Eta] - 1] += 1

        for __Theta in range(1, n + 1):
            bfs(__Theta)

        return __Alpha