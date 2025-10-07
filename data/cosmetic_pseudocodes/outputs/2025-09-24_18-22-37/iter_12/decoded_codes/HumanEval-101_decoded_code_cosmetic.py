from typing import List


def words_string(w1: str) -> List[str]:
    if not w1:
        return []

    L1: List[str] = []

    I1 = 0
    while I1 < len(w1):
        C1 = w1[I1]
        if C1 == ",":
            L1.append(" ")
        else:
            L1.append(C1)
        I1 += 1

    R1 = ""
    for E1 in L1:
        R1 += E1

    R2 = R1.split()
    return R2