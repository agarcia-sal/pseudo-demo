class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        def calc(a: int, b: int) -> int:
            if a == b:
                return 0
            if a < b:
                if a == 0 and b == 2:
                    return 1
                return -1
            else:
                if a == 2 and b == 0:
                    return -1
                return 1

        @lru_cache(None)
        def dfs(x: int, y: int, z: int) -> int:
            # If remaining characters are fewer or equal than y, no valid sequences
            if (len(s) - x) <= y:
                return 0
            if x >= len(s):
                return 1 if y < 0 else 0

            accumulator = 0
            for index in range(3):
                if index == z:
                    continue
                tempVal = calc(d[s[x]], index)
                accumulator += dfs(x + 1, y + tempVal, index)
            return accumulator % mod

        answer = dfs(0, 0, -1)
        dfs.cache_clear()
        return answer