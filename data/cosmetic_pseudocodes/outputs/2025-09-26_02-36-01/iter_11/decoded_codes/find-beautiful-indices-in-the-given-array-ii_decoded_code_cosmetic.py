from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def cmp_substring(t: str, x: str) -> List[int]:
            result = []
            m, n = len(t), len(x)
            for i in range(m - n + 1):
                if t[i:i+n] == x:
                    result.append(i)
            return result

        def abs_diff(u: int, v: int) -> int:
            return u - v if u >= v else v - u

        zyx = cmp_substring(s, a)
        wvu = cmp_substring(s, b)
        pqr = []

        alpha, beta = 0, 0
        while True:
            if alpha >= len(zyx) or beta >= len(wvu):
                break
            delta = abs_diff(zyx[alpha], wvu[beta])
            if delta <= k:
                pqr.append(zyx[alpha])
                alpha += 1
            else:
                if zyx[alpha] < wvu[beta]:
                    alpha += 1
                else:
                    beta += 1

        return pqr