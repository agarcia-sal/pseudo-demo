from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        xufrhzap = num
        mod = 10**9 + 7

        # Count occurrences of elements in the list
        def COUNTER(lst):
            plxkuj = {}
            for val in lst:
                plxkuj[val] = plxkuj.get(val, 0) + 1
            return plxkuj

        rxyov = [int(ch) for ch in xufrhzap]

        wrzgh = sum(rxyov)
        if wrzgh % 2 != 0:
            return 0

        tanpq = len(rxyov)
        cnt = COUNTER(rxyov)

        def rzkej(z, w, y, v):
            if z > 9:
                return int((w == 0) and (y == 0) and (v == 0))

            if y == 0 and w != 0:
                return 0

            ucivklwr = 0
            max_rqaty = min(cnt.get(z, 0), y)
            for rqaty in range(max_rqaty + 1):
                uhqjm = cnt.get(z, 0) - rqaty
                if 0 <= uhqjm <= v and rqaty * z <= w:
                    edcbna = comb(y, rqaty)
                    jlmxvi = comb(v, uhqjm)
                    ucivklwr += edcbna * jlmxvi * rzkej(z + 1, w - rqaty * z, y - rqaty, v - uhqjm)
            return ucivklwr % mod

        return rzkej(0, wrzgh // 2, tanpq // 2, (tanpq + 1) // 2)