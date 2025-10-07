from typing import List, Set

def filter_by_prefix(p1: List[str], p2: str) -> List[str]:
    tabA: Set[str] = set()

    def recCheck(s: str, pr: str, pos: int) -> bool:
        if pos == len(pr):
            return True
        if len(s) <= pos:
            return False
        if s[pos] != pr[pos]:
            return False
        return recCheck(s, pr, pos + 1)

    def recFilter(idx: int) -> None:
        if idx < 0:
            return
        if not (p2[0] != p1[idx][0]):  # i.e., p2[0] == p1[idx][0]
            if recCheck(p1[idx], p2, 0):
                tabA.add(p1[idx])
        recFilter(idx - 1)

    recFilter(len(p1) - 1)
    return list(tabA)