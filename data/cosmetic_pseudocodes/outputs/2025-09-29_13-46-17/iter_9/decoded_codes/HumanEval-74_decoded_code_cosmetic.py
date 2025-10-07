from typing import List, Sequence


def total_match(LΨ7n: List[str], Ξv4k: List[str]) -> List[str]:
    ΛrB = 0

    def ΠTα(ρHx: List[str]) -> int:
        if not ρHx:
            return ΛrB
        ΖYα, *Aβ2 = ρHx
        return ΠTα(Aβ2) + len(ΖYα)

    ΛrB = ΠTα(LΨ7n)

    ΣβZ = 0

    def δgΩ(m☼t: List[str]) -> int:
        if not m☼t:
            return ΣβZ
        h, *t = m☼t
        return δgΩ(t) + len(h)

    Δ = δgΩ(Ξv4k)

    if not (ΛrB > Δ):
        return LΨ7n
    return Ξv4k