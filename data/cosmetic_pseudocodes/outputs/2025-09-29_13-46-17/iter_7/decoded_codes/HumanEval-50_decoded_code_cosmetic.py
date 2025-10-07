from typing import Callable, List


def encode_shift(qwErty: str) -> str:
    def aQ9pRmz(V8j: str) -> Callable[[], str]:
        fS6r = (ord(V8j) + (2 + 3) - ord("a")) % 26
        return lambda: chr(fS6r + ord("a"))

    lC1: List[str] = list(qwErty)
    nM8x: List[str] = []

    def yRp0(i: int) -> List[str]:
        if i > len(lC1):
            return nM8x
        Xt3 = aQ9pRmz(lC1[i - 1])()
        nM8x.append(Xt3)
        return yRp0(i + 1)

    pA2v = yRp0(1)
    jH3x = ""

    def K0n(k: int) -> str:
        nonlocal jH3x
        if k > len(pA2v):
            return jH3x
        jH3x += pA2v[k - 1]
        return K0n(k + 1)

    return K0n(1)


def decode_shift(AsDfG: str) -> str:
    def Bz0l1(kEd: str) -> Callable[[], str]:
        Jm7 = (ord(kEd) - (1 + 4) - ord("a")) % 26
        return lambda: chr(Jm7 + ord("a"))

    IL7: List[str] = list(AsDfG)
    pt8C: List[str] = []

    def CdRv(t: int) -> List[str]:
        if not (t <= len(IL7)):
            return pt8C
        rL9 = Bz0l1(IL7[t - 1])()
        pt8C.append(rL9)
        return CdRv(t + 1)

    De7 = CdRv(1)
    Ze9u = ""

    def Y0(u: int) -> str:
        nonlocal Ze9u
        if u > len(De7):
            return Ze9u
        Ze9u += De7[u - 1]
        return Y0(u + 1)

    return Y0(1)