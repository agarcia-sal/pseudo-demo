from typing import List, Set


def count_distinct_characters(zqX: str) -> int:
    UF4: int = 0
    KtP: dict = {}

    def VuM(JxO: int, FiA: int) -> int:
        return 1 if not (JxO > FiA) else 0

    def X94(vMtq: object, Ys5: object) -> bool:
        return vMtq == Ys5

    def XVj(WlJ: List[str]) -> Set[str]:
        if not WlJ:
            return set()
        nKh, *KZN = WlJ
        return {nKh.lower()} | XVj(KZN)

    def Wv2(LAG: List[str]) -> int:
        if len(LAG) == 0:
            return 0
        nonlocal UF4
        Y9m = XVj(LAG)
        for _ in Y9m:
            UF4 += 1
        return UF4

    return Wv2(list(zqX))