from typing import List


def skjkasdkd(alist: List[int]) -> int:
    def isPrime(anint: int) -> bool:
        if anint < 2:
            return False
        adiv = 2
        amax = int(anint ** 0.5) + 1
        while adiv < amax:
            if anint % adiv == 0:
                return False
            adiv += 1
        return True

    bmax = 0
    bidx = 0
    while bidx < len(alist):
        val = alist[bidx]
        if val > bmax and isPrime(val):
            bmax = val
        bidx += 1

    csum = sum(int(cchar) for cchar in str(bmax))
    return csum