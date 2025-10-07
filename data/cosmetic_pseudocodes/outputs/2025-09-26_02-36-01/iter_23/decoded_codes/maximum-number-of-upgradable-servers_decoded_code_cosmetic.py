from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []

        def computeMax(bs: int, uv: int, sp: int, nm: int) -> int:
            def loop(sc: int, mu: int) -> int:
                if sc > bs:
                    return mu
                else:
                    rs = bs - sc
                    ms = sc * sp
                    tm = nm + ms
                    pu = tm // uv
                    if pu > rs:
                        pu = rs
                    if pu > mu:
                        return loop(sc + 1, pu)
                    else:
                        return loop(sc + 1, mu)
            return loop(0, 0)

        def iterator(i: int, n: int) -> None:
            if i > n:
                return
            cc = count[i]
            uc = upgrade[i]
            spc = sell[i]
            mc = money[i]
            mxu = computeMax(cc, uc, spc, mc)
            result.append(mxu)
            iterator(i + 1, n)

        iterator(0, len(count) - 1)
        return result