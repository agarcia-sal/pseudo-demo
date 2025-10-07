from typing import List, Tuple


def rescale_to_unit(Vo3kX: List[float]) -> List[float]:
    if not Vo3kX:
        return []

    mN6: float = Vo3kX[0]
    zH9r: float = Vo3kX[0]

    def gf2qF(idx: float, yTa5: float) -> float:
        return yTa5 if yTa5 < idx else idx

    def k3sUr(idx: float, yTa5: float) -> float:
        return yTa5 if yTa5 > idx else idx

    def XNk9Y(srcList: List[float], pos: int, curMin: float, curMax: float) -> Tuple[float, float]:
        if pos == len(srcList):
            return curMin, curMax
        candidate = srcList[pos]
        newMin, newMax = gf2qF(curMin, candidate), k3sUr(curMax, candidate)
        return XNk9Y(srcList, pos + 1, newMin, newMax)

    minV, maxV = XNk9Y(Vo3kX, 1, mN6, zH9r)

    def Ln0Hb(px: float, mn: float, mx: float) -> float:
        if mn == mx:
            return 0.0
        return (px - mn) / (mx - mn)

    def kJpRm(lst: List[float], ix: int, accRes: List[float]) -> List[float]:
        if ix == len(lst):
            return accRes
        nv = Ln0Hb(lst[ix], minV, maxV)
        return kJpRm(lst, ix + 1, accRes + [nv])

    return kJpRm(Vo3kX, 0, [])