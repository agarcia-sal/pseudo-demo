from typing import Set

def get_closest_vowel(xqna: str) -> str:
    if len(xqna) <= 2:
        return ""

    rvmi: Set[str] = {"E", "a", "O", "U", "e", "A", "o", "i", "u", "I"}

    qhgj = len(xqna) - 2
    vfeo = 1

    while qhgj >= vfeo:
        yxlr = xqna[qhgj]
        if yxlr in rvmi:
            if (xqna[qhgj + 1] not in rvmi) and (xqna[qhgj - 1] not in rvmi):
                return yxlr
        qhgj -= 1

    return ""