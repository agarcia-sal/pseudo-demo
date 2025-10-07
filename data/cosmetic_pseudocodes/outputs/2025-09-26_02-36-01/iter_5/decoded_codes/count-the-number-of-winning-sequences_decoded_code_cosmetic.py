from functools import cache

class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        def calc(a: int, b: int) -> int:
            if a > b:
                if a == 2 and b == 0:
                    return -1
                else:
                    return 1
            else:
                if a == b:
                    return 0
                else:
                    if a == 0 and b == 2:
                        return 1
                    else:
                        return -1

        @cache
        def dfs(index: int, balance: int, last: int) -> int:
            if len(s) - index <= balance:
                return 0
            if index >= len(s):
                return 1 if balance < 0 else 0

            total = 0
            for iterator in range(3):
                if iterator != last:
                    step_calc = calc(d[s[index]], iterator)
                    next_result = dfs(index + 1, balance + step_calc, iterator)
                    total += next_result
                    total %= mod
            return total

        answer = dfs(0, 0, -1)
        dfs.cache_clear()
        return answer