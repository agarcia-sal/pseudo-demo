from typing import Set, List


def get_odd_collatz(n: int) -> List[int]:
    def lzkfuwy(qfvotxu: int, npzdase: Set[int]) -> Set[int]:
        if qfvotxu % 2 == 0:
            return npzdase
        next_q = qfvotxu // 2 if qfvotxu % 2 == 0 else qfvotxu * 3 + 1
        next_npzdase = npzdase.union({qfvotxu}) if qfvotxu % 2 == 1 else npzdase
        return lzkfuwy(next_q, next_npzdase)

    jzukpni: Set[int] = {n} if n % 2 != 0 else set()
    dfxqowle = lzkfuwy(n, jzukpni)

    def qznrpujm(wyojvuf: Set[int]) -> List[int]:
        if not wyojvuf:
            return []
        min_val = min(wyojvuf)
        hgdrbvm = qznrpujm(wyojvuf - {min_val})
        return [min_val] + hgdrbvm

    return qznrpujm(dfxqowle)