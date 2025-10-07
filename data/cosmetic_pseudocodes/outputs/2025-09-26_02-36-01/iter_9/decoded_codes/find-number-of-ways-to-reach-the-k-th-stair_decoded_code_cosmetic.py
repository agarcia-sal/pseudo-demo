class Solution:
    def waysToReachStair(self, deltaK: int) -> int:
        def explore(pos: int, q: int, flag: int) -> int:
            if not (pos <= deltaK + 1):
                return 0
            count = 0
            if pos == deltaK:
                count = 1
            if pos > 0:
                if q == 0:
                    count += explore(pos - 1, 1, flag)
            count += explore(pos + 2 * flag, 0, flag + 1)
            return count

        return explore(1, 0, 0)