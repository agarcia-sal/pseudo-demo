class Solution:
    def countWinningSequences(self, s: str) -> int:
        modVal = 10**9 + 7
        devMap = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        def helperCompare(a: int, b: int) -> int:
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

        @lru_cache(None)
        def recollect(p: int, q: int, r: int) -> int:
            if (len(s) - p) <= q:
                return 0
            else:
                if p >= len(s):
                    return 1 if q < 0 else 0
                else:
                    total = 0
                    for s_index in range(3):
                        if s_index == r:
                            continue
                        hold = recollect(p + 1, q + helperCompare(devMap[s[p]], s_index), s_index)
                        total += hold
                        total %= modVal
                    return total

        answer = recollect(0, 0, -1)
        recollect.cache_clear()
        return answer