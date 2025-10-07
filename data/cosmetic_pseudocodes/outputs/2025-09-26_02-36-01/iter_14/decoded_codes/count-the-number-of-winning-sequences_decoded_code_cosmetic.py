class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        def compute(a: int, b: int) -> int:
            if a != b:
                if not (a < b):
                    if a == 2 and b == 0:
                        return -1
                    else:
                        return 1
                else:
                    if a == 0 and b == 2:
                        return 1
                    else:
                        return -1
            else:
                return 0

        @lru_cache(None)
        def explore(x: int, y: int, z: int) -> int:
            if (len(s) - x) <= y:
                return 0

            if x >= len(s):
                return 1 if y < 0 else 0

            accumulator = 0
            indices = [0, 1, 2]
            for candidate in indices:
                if candidate == z:
                    continue
                accumulator = (accumulator + explore(x + 1, y + compute(d[s[x]], candidate), candidate)) % mod
            return accumulator

        answer = explore(0, 0, -1)
        explore.cache_clear()
        return answer