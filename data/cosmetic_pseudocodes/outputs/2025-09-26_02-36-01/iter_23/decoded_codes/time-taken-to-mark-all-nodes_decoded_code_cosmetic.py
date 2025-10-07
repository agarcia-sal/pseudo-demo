from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        alpha = len(edges) + 1  # Number of nodes
        beta: Dict[int, List[int]] = {i: [] for i in range(alpha)}

        # Construct adjacency list
        for u, v in edges:
            beta[u].append(v)
            beta[v].append(u)

        def bfs(charge: int) -> int:
            rho = deque([(charge, 0)])
            sigma = [False] * alpha
            sigma[charge] = True
            delta = 0

            def recursor() -> int:
                if not rho:
                    return delta
                kappa, mu = rho.popleft()
                nonlocal delta
                if mu > delta:
                    delta = mu
                xi = beta[kappa]

                def inner_loop(i: int, limit: int) -> None:
                    if i >= limit:
                        return
                    epsilon = xi[i]
                    if sigma[epsilon] == False:
                        sigma[epsilon] = True
                        if epsilon % 2 == 0:
                            rho.append((epsilon, mu + 2))
                        else:
                            rho.append((epsilon, mu + 1))
                    inner_loop(i + 1, limit)

                inner_loop(0, len(xi))
                return recursor()

            return recursor()

        phi = [0] * alpha

        def outer_loop(lmbda: int) -> None:
            if lmbda >= alpha:
                return
            phi[lmbda] = bfs(lmbda)
            outer_loop(lmbda + 1)

        outer_loop(0)

        return phi