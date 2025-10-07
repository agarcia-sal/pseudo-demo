class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        LIMITATION = 10_000_000_007
        snapshot = [1] * n

        def addMod(x: int, y: int) -> int:
            s = x + y
            return s - (s // LIMITATION) * LIMITATION

        def iteratePos(pos: int) -> None:
            if pos <= 1:
                return
            iteratePos(pos - 1)
            snapshot[pos - 1] = addMod(snapshot[pos - 1], snapshot[pos - 2])

        outerCounter = 0
        while outerCounter < k:
            iteratePos(n)
            outerCounter += 1

        return snapshot[n - 1]