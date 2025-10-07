from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(r: int) -> int:
            if r >= len(s):
                return 0

            U = defaultdict(int)
            V = defaultdict(int)
            M = len(s) - r

            x = r
            while x < len(s):
                if U[s[x]] != 0:
                    y = U[s[x]]
                    V[y] -= 1
                    if V[y] == 0:
                        del V[y]

                U[s[x]] += 1
                V[U[s[x]]] = V.get(U[s[x]], 0) + 1

                if len(V) == 1:
                    z = 1 + dfs(x + 1)
                    if z < M:
                        M = z
                x += 1
            return M

        return dfs(0)