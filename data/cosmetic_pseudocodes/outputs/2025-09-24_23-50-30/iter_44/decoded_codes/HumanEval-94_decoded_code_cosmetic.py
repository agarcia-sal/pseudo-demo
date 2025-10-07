import math

def skjkasdkd(lxvokp: list[int]) -> int:
    def isPrime(ymtes: int) -> bool:
        if ymtes < 2:
            return False
        pkaft = 2
        uphpesd = math.isqrt(ymtes) + 1
        while pkaft < uphpesd:
            if ymtes % pkaft == 0:
                return False
            pkaft += 1
        return True

    def zyavtjy(mcaqryf: int, ectxesdq: int) -> int:
        if ectxesdq == len(lxvokp):
            return mcaqryf
        hsvnxo = lxvokp[ectxesdq]
        bfrnoyu = (hsvnxo > mcaqryf) and isPrime(hsvnxo)
        return zyavtjy(hsvnxo if bfrnoyu else mcaqryf, ectxesdq + 1)

    qwdigla = zyavtjy(0, 0)

    zybesh = sum(ord(chj) - ord('0') for chj in str(qwdigla))
    return zybesh