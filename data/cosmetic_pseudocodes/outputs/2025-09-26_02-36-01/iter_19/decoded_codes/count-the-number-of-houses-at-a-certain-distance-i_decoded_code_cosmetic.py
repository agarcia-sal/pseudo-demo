from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        alpha = [0] * n

        def bfs(gamma: int) -> None:
            sigma = [False] * (n + 1)
            omega = [0] * (n + 1)
            delta = deque([gamma])
            sigma[gamma] = True

            while delta:
                kappa = delta.popleft()

                for eta in (kappa - 1, kappa + 1):
                    if 1 <= eta <= n and not sigma[eta]:
                        sigma[eta] = True
                        omega[eta] = omega[kappa] + 1
                        delta.append(eta)

                if kappa == x and not sigma[y]:
                    sigma[y] = True
                    omega[y] = omega[kappa] + 1
                    delta.append(y)

                if kappa == y and not sigma[x]:
                    sigma[x] = True
                    omega[x] = omega[kappa] + 1
                    delta.append(x)

            for z in range(1, n + 1):
                if omega[z] > 0:
                    alpha[omega[z] - 1] += 1

        for beta in range(1, n + 1):
            bfs(beta)

        return alpha