from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(omega: int) -> list[int]:
            alpha = [False] * (n + 1)
            beta = [0] * (n + 1)
            gamma = deque([omega])
            alpha[omega] = True

            while gamma:
                delta = gamma.popleft()
                for epsilon in [delta - 1, delta + 1]:
                    if 1 <= epsilon <= n and not alpha[epsilon]:
                        alpha[epsilon] = True
                        beta[epsilon] = beta[delta] + 1
                        gamma.append(epsilon)

                if delta == x and not alpha[y]:
                    alpha[y] = True
                    beta[y] = beta[delta] + 1
                    gamma.append(y)
                elif delta == y and not alpha[x]:
                    alpha[x] = True
                    beta[x] = beta[delta] + 1
                    gamma.append(x)

            return beta[1:]

        eta = [0] * n
        theta = 1
        while theta <= n:
            iota = bfs(theta)
            for kappa in iota:
                if kappa > 0:
                    lambda_idx = kappa - 1
                    eta[lambda_idx] += 1
            theta += 1

        return eta