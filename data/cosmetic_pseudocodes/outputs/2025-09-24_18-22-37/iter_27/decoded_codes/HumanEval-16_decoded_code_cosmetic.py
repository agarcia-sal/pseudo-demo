from typing import Set


def count_distinct_characters(alp: str) -> int:
    vje: str = alp.lower()
    rqx: Set[str] = set()
    cnm: int = 0
    while cnm < len(vje):
        tgz: str = vje[cnm]
        rqx |= {tgz}
        cnm += 1
    dkq: int = len(rqx)
    return dkq