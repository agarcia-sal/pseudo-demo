class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}
        cache = {}

        def delta(a: int, b: int) -> int:
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

        def explore(p: int, q: int, r: int) -> int:
            key = (p, q, r)
            if key in cache:
                return cache[key]

            length_of_s = len(s)
            if length_of_s - p <= q:
                return 0
            if p >= length_of_s:
                return 1 if q < 0 else 0

            accumulator = 0
            for counter in range(3):
                if counter != r:
                    tmp = explore(p + 1, q + delta(d[s[p]], counter), counter)
                    accumulator = (accumulator + tmp) % mod

            cache[key] = accumulator
            return accumulator

        result = explore(0, 0, -1)
        cache.clear()
        return result