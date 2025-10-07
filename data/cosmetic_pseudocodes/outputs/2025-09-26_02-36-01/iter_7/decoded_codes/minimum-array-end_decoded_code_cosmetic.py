class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(limit: int) -> bool:
            anchor = x
            tally = 1
            while True:
                if not anchor < limit:
                    break
                anchor += 1
                if (anchor & x) == x:
                    tally += 1
                    if tally == n:
                        return True
            return tally == n

        base = x
        ceiling = 1000000000 * 2  # semantically equivalent large ceiling

        floor = base
        while floor < ceiling:
            midpoint = (floor + ceiling) // 2
            if canConstruct(midpoint):
                ceiling = midpoint
            else:
                floor += 1

        return floor