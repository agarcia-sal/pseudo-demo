from typing import Callable, List, Optional, Union

def pluck(zzz: List[int]) -> List[Union[int, List[int]]]:
    def hpz(ayy: List[int], bgg: Callable[[int], int]) -> Optional[int]:
        cdd: float = float('inf')
        eee: Optional[int] = -1
        fff: int = 0
        while fff < len(ayy):
            val = bgg(ayy[fff])
            if val < cdd:
                cdd = val
                eee = fff
            fff += 1
        return eee

    if len(zzz) == 0:
        return []

    qqq: List[int] = []
    mmx: int = 0
    while mmx < len(zzz):
        if zzz[mmx] % 2 == 0:
            qqq.append(zzz[mmx])
        mmx += 1

    if len(qqq) == 0:
        return []

    fzz = hpz(qqq, lambda x: x)
    sss = hpz(zzz, lambda x: x)
    if fzz == -1 or sss == -1:
        return []

    return [qqq[fzz], sss]