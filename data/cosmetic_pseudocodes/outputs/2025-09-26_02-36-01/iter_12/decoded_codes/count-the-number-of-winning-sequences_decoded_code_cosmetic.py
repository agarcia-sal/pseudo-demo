from functools import cache

class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 1_000_000_007
        d = {'F': 0, 'W': 1, 'E': 2}

        def computeDelta(a: int, b: int) -> int:
            if a < b:
                if a != 0 or b != 2:
                    return -1
                else:
                    return 1
            elif a > b:
                if a == 2 and b == 0:
                    return -1
                else:
                    return 1
            else:
                return 0

        @cache
        def walk(index: int, balance: int, prev: int) -> int:
            if balance > len(s) - index:
                return 0
            if index >= len(s):
                return 1 if balance < 0 else 0

            accumulator = 0

            def loopOverValues(counter: int) -> None:
                nonlocal accumulator
                if counter > 2:
                    return
                if counter != prev:
                    accumulator = (accumulator + walk(index + 1, balance + computeDelta(d[s[index]], counter), counter)) % mod
                loopOverValues(counter + 1)

            loopOverValues(0)

            return accumulator

        result = walk(0, 0, -1)
        walk.cache_clear()
        return result