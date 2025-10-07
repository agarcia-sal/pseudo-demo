from functools import cache

class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {"F": 0, "W": 1, "E": 2}

        def calc(p: int, q: int) -> int:
            if p != q:
                if p < q:
                    if p == 0:
                        if q == 2:
                            return 1
                        else:
                            return -1
                    else:
                        return -1
                else:
                    if p == 2 and q == 0:
                        return -1
                    else:
                        return 1
            else:
                return 0

        @cache
        def dfs(a: int, b: int, c: int) -> int:
            if (len(s) - a) <= b:
                return 0
            if a >= len(s):
                return 1 if b < 0 else 0

            total_results = 0
            for current_index in range(3):
                if current_index == c:
                    continue
                delta = calc(d[s[a]], current_index)
                subtotal = dfs(a + 1, b + delta, current_index)
                total_results = (total_results + subtotal) % mod
            return total_results

        answer = dfs(0, 0, -1)
        dfs.cache_clear()
        return answer