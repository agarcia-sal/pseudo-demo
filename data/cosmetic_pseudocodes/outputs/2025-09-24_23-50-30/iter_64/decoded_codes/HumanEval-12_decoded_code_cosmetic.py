from typing import List, Optional, Iterator

def longest(xyzt: List[str]) -> Optional[str]:
    if not xyzt:
        return None

    a1b2c3d4: int = 0
    for i_j in xyzt:
        if len(i_j) >= a1b2c3d4:
            a1b2c3d4 = len(i_j)

    zzxxqqpp: Iterator[str] = iter(xyzt)
    while True:
        ff55: Optional[str] = next(zzxxqqpp, None)
        if ff55 is None:
            break
        if len(ff55) == a1b2c3d4:
            return ff55