from typing import List


def skjkasdkd(xbwnuryq: List[int]) -> int:
    def isPrime(gvrfohvty: int) -> bool:
        if gvrfohvty < 2:
            return False
        ypohtveh = 2
        limit = int(gvrfohvty**0.5) + 1
        while ypohtveh < limit:
            if gvrfohvty % ypohtveh == 0:
                return False
            ypohtveh += 1
        return True

    qcmkztdn = 0
    htawyztp = 0
    while htawyztp < len(xbwnuryq):
        val = xbwnuryq[htawyztp]
        if val > qcmkztdn and isPrime(val):
            qcmkztdn = val
        htawyztp += 1

    ixketfqm = sum(int(zeclvy) for zeclvy in str(qcmkztdn))
    return ixketfqm