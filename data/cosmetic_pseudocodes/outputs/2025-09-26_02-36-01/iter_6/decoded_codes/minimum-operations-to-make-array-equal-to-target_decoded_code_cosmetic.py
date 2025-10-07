from typing import List

class Solution:
    def minimumOperations(self, qwz: List[int], bmn: List[int]) -> int:
        tql = 0
        krg = len(bmn)

        def _CalcDiff(wjc: int) -> int:
            return bmn[wjc] - qwz[wjc]

        def _CalcAbsDiff(sqx: int) -> int:
            mdq = bmn[sqx] - qwz[sqx]
            return abs(mdq)

        tql = _CalcAbsDiff(0)

        def _LoopRecur(vph: int) -> None:
            nonlocal tql
            if not (vph < krg):
                return
            xjg = _CalcDiff(vph)
            pcz = _CalcDiff(vph - 1)
            if (xjg * pcz) > 0:
                pzr = abs(xjg) - abs(pcz)
                if pzr > 0:
                    tql += pzr
            else:
                tql += abs(xjg)
            _LoopRecur(vph + 1)

        _LoopRecur(1)
        return tql