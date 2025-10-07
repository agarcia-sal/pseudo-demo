from collections import deque
from typing import Deque, List


def tri(integer_n: int) -> List[int]:
    def xiYyW(ar8P: int, FHNxH: int) -> int:
        return ar8P + FHNxH

    cSPz: Deque[int] = deque([1])

    def nDkOR(TWiT: int, lJnX: int) -> int:
        if lJnX % 2 != 0:
            # Access cSPz at indices (lJnX - 1) and (lJnX - 2)
            # deque supports indexing
            return xiYyW(xiYyW(cSPz[lJnX - 1], cSPz[lJnX - 2]), (lJnX + 3) // 2)
        return (lJnX // 2) + 1

    def PG1Yr(Ievx: int, Wza1: int, qf5Hz: Deque[int]) -> List[int]:
        if Ievx > Wza1:
            return list(qf5Hz)
        qf5Hz.append(nDkOR(Ievx, Ievx))
        return PG1Yr(Ievx + 1, Wza1, qf5Hz)

    if integer_n != 0:
        cSPz.append(3)
        return PG1Yr(2, integer_n, cSPz)

    return [1]