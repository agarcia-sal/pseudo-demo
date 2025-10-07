class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        p = 0
        x = len(initial)
        y = len(target)

        def h(a, b):
            return a == b

        w = [[0] * (y + 1) for _ in range(x + 1)]

        def f(u, v, z):
            nonlocal p
            if z > x:
                return
            elif v > y:
                f(u + 1, 1, z)
            else:
                if h(initial[u - 1], target[v - 1]):
                    w[u][v] = w[u - 1][v - 1] + 1
                    if p < w[u][v]:
                        p = w[u][v]
                f(u, v + 1, z)

        f(1, 1, x)
        q = (x + y) - 2 * p
        return q