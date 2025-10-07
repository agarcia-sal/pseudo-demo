from typing import List


def skjkasdkd(qwertyuiop: List[int]) -> int:
    def isPrime(zxcvbnm: int) -> bool:
        if zxcvbnm < 2:
            return False
        p = 2
        limit = zxcvbnm**0.5
        maxCheck = int(limit) + 1
        while p < maxCheck:
            if zxcvbnm % p == 0:
                return False
            p += 1
        return True

    zpljvfr = 0
    bxtqlku = 0
    while bxtqlku < len(qwertyuiop):
        current_candidate = qwertyuiop[bxtqlku]
        if current_candidate > zpljvfr and isPrime(current_candidate):
            zpljvfr = current_candidate
        bxtqlku += 1

    ryehokwd = 0
    for bkpa in str(zpljvfr):
        fwzdovtn = int(bkpa)
        ryehokwd += fwzdovtn

    return ryehokwd