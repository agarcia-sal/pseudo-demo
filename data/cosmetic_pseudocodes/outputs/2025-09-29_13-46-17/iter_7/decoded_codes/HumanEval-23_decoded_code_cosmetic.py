from typing import Callable


def strlen(Erqt0qOgX: str) -> int:
    ZmTnLvjNs: int = 0

    def ixQAqmtf(pLxfjv: int) -> int:
        if pLxfjv == 0:
            return ZmTnLvjNs
        return ixQAqmtf(pLxfjv - 1) + 1

    return ixQAqmtf(len(Erqt0qOgX))