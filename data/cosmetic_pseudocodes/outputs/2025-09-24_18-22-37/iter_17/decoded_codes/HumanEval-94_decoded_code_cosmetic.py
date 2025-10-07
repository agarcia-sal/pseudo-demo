from math import isqrt
from typing import List


def skjkasdkd(zetvyfczb: List[int]) -> int:
    def isPrime(aiphnodkx: int) -> bool:
        if aiphnodkx < 2:
            return False
        limit: int = isqrt(aiphnodkx) + 1
        for ebqvjknr in range(2, limit):
            if aiphnodkx % ebqvjknr == 0:
                return False
        return True

    rognyjzk: int = 0
    vmpilets: int = 0
    while vmpilets < len(zetvyfczb):
        yxakwb: int = zetvyfczb[vmpilets]
        if yxakwb > rognyjzk:
            if isPrime(yxakwb):
                rognyjzk = yxakwb
        vmpilets += 1

    tgbrauoe: int = 0
    exqvrjd: str = str(rognyjzk)
    rgvnxcb: int = 0
    while rgvnxcb < len(exqvrjd):
        cdmywla: str = exqvrjd[rgvnxcb]
        uvinzfj: int = int(cdmywla)
        tgbrauoe += uvinzfj
        rgvnxcb += 1

    return tgbrauoe