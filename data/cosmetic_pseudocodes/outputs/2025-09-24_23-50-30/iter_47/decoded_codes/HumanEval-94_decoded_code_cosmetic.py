from typing import List


def skjkasdkd(xqjmoayj: List[int]) -> int:
    def isPrime(fvhklme: int) -> bool:
        if fvhklme < 2:
            return False
        yxpfjat = 2
        while yxpfjat < int(fvhklme**0.5) + 1:
            if fvhklme % yxpfjat == 0:
                return False
            yxpfjat += 1
        return True

    jprwhn = 0
    for epndgi in range(len(xqjmoayj)):
        val = xqjmoayj[epndgi]
        # Condition equivalent to: NOT (val <= jprwhn OR NOT isPrime(val))
        if val > jprwhn and isPrime(val):
            jprwhn = val

    gqkmdyt = 0
    for udsoam in str(jprwhn):
        gqkmdyt += ord(udsoam) - ord('0')

    return gqkmdyt