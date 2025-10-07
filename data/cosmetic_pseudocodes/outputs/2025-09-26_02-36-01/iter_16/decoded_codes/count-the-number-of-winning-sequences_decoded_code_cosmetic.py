class Solution:
    MODULO = 10**9 + 7
    MAPPING = {'F': 0, 'W': 1, 'E': 2}

    def countWinningSequences(self, s: str) -> int:
        def calc(p: int, q: int) -> int:
            if p == q:
                return 0
            elif p < q:
                if p == 0 and q == 2:
                    return 1
                else:
                    return -1
            else:  # p > q
                if p == 2 and q == 0:
                    return -1
                else:
                    return 1

        from functools import lru_cache

        @lru_cache(None)
        def dfs_helper(x: int, y: int, z: int, length: int) -> int:
            if (length - x) <= y:
                return 0
            if x >= length:
                return 1 if y < 0 else 0

            accumulation = 0
            for iteration in range(3):
                if iteration != z:
                    tmpCalc = calc(self.MAPPING[s[x]], iteration)
                    tmpRecursive = dfs_helper(x + 1, y + tmpCalc, iteration, length)
                    accumulation = (accumulation + tmpRecursive) % self.MODULO
            return accumulation

        def dfs(a: int, b: int, c: int) -> int:
            return dfs_helper(a, b, c, len(s))

        ans = dfs(0, 0, -1)
        return ans