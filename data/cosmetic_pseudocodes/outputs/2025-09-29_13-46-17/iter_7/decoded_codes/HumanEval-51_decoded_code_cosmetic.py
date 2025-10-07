from typing import Set

def remove_vowels(e2XJb: str) -> str:
    tb5k: Set[str] = {"u", "i", "a", "o", "e"}

    def N9qLf(Yvcz: str) -> bool:
        return Yvcz not in tb5k

    def lDO8w(idx: int, QMoX: str) -> str:
        if idx > len(e2XJb):
            return QMoX
        p0A: str = e2XJb[idx - 1].lower()  # idx is 1-based in the pseudocode
        if N9qLf(p0A):
            return lDO8w(idx + 1, QMoX + e2XJb[idx - 1])
        else:
            return lDO8w(idx + 1, QMoX)

    return lDO8w(1, "")