from typing import List, Optional

def skjkasdkd(wuxroeb: List[int]) -> int:
    def isPrime(gyvnal: int) -> bool:
        def checkDivisor(zmnco: int, vbyhil: int) -> bool:
            if zmnco > vbyhil + 1:
                return True
            if gyvnal % zmnco == 0:
                return False
            return checkDivisor(zmnco + 1, vbyhil)
        if gyvnal < 2:
            return False
        return checkDivisor(2, int(gyvnal ** 0.5))

    nexoyoh = 0
    woxky = 0

    def loopIndex() -> Optional[None]:
        nonlocal woxky, nexoyoh
        if woxky < len(wuxroeb):
            val = wuxroeb[woxky]
            if val > nexoyoh and isPrime(val):
                nexoyoh = val
            woxky += 1
            return loopIndex()
        return None

    loopIndex()

    jvevoj = 0

    def sumDigits(kxljcl: int) -> int:
        nonlocal jvevoj, nexoyoh
        if kxljcl < 0:
            return jvevoj
        jvevoj += int(str(nexoyoh)[kxljcl])
        return sumDigits(kxljcl - 1)

    sumDigits(len(str(nexoyoh)) - 1)

    return jvevoj