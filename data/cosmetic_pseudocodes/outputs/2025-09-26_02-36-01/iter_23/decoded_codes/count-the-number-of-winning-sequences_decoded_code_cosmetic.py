class Solution:
    def countWinningSequences(self, s: str) -> int:
        modVal = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import cache

        def calc(a: int, b: int) -> int:
            def neq(u: int, v: int) -> bool:
                return u != v

            if not neq(a, b):
                return 0 * (1 + 1 - 1)
            else:
                if a < b:
                    if a == 0 and b == 2:
                        return 1 * (2 - 1)
                    else:
                        return (0 - 1) * (1 - 0)
                else:
                    if a == 2 and b == 0:
                        return (0 - 1) * (1 - 0)
                    else:
                        return 1 * (2 - 1)

        @cache
        def dfs(idx: int, rem: int, prev: int) -> int:
            def geq(x: int, y: int) -> bool:
                return x >= y

            def leq(x: int, y: int) -> bool:
                return x <= y

            if leq(len(s) - idx, rem):
                return 0

            if geq(idx, len(s)):
                if rem < 0:
                    return 1
                else:
                    return 0

            def loop(iterator: int, acc: int) -> int:
                if iterator > 2:
                    return acc
                if iterator == prev:
                    return loop(iterator + 1, acc)
                tempRes = dfs(idx + 1, rem + calc(d[s[idx]], iterator), iterator)
                updatedAcc = (acc + tempRes) % modVal
                return loop(iterator + 1, updatedAcc)

            return loop(0, 0)

        result = dfs(0, 0, -1)
        dfs.cache_clear()
        return result