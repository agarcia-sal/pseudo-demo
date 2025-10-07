class Solution:
    def countWinningSequences(self, inputString: str) -> int:
        modValue = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import cache

        def calc(a: int, b: int) -> int:
            if a == b:
                return 0
            if a < b:
                if a == 0 and b == 2:
                    return 1
                else:
                    return -1
            if a == 2 and b == 0:
                return -1
            else:
                return 1

        @cache
        def dfs(idx: int, balance: int, prev: int) -> int:
            if len(inputString) - idx <= balance:
                return 0
            if idx >= len(inputString):
                return 1 if balance < 0 else 0

            resVar = 0
            for loopVar in range(3):
                if loopVar == prev:
                    continue
                partial = dfs(idx + 1, balance + calc(d[inputString[idx]], loopVar), loopVar)
                resVar = (resVar + partial) % modValue
            return resVar

        answer = dfs(0, 0, -1)
        dfs.cache_clear()
        return answer