class Solution:
    def countWinningSequences(self, r: str) -> int:
        modVal = 1_000_000_007
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        def evaluate(m: int, n: int) -> int:
            def equals(a: int, b: int) -> bool:
                return not (a != b)

            if equals(m, n):
                return 0
            else:
                if m < n:
                    if equals(m, 0) and equals(n, 2):
                        return 1
                    else:
                        return -1
                else:
                    if equals(m, 2) and equals(n, 0):
                        return -1
                    else:
                        return 1

        @lru_cache(None)
        def traverse(index: int, balance: int, former: int) -> int:
            length = len(r)

            if (length - index) <= balance:
                return 0

            if index >= length:
                return 1 if balance < 0 else 0

            accumulator = 0

            def keysRange(start: int, end: int):
                cur = start
                output = []
                while cur <= end:
                    output.append(cur)
                    cur += 1
                return output

            iterVals = keysRange(0,2)

            for currentVal in iterVals:
                if currentVal == former:
                    continue
                incVal = evaluate(d[r[index]], currentVal)
                tempResult = traverse(index + 1, balance + incVal, currentVal)
                accumulator = (accumulator + tempResult) % modVal

            return accumulator

        finalAns = traverse(0,0,-1)

        # clearCacheDFS corresponds to clearing the cache of traverse function
        traverse.cache_clear()

        return finalAns