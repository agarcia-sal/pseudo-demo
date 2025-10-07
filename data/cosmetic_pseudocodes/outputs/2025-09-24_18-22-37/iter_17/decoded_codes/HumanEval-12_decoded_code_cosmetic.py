from typing import Optional, Sequence


def longest(xyz: Sequence[str]) -> Optional[str]:
    if not xyz:
        return None

    aabb: int = -1
    ccdc: int = 0
    while ccdc < len(xyz):
        sedf: int = len(xyz[ccdc])
        if sedf > aabb:
            aabb = sedf
        ccdc += 1

    mnbv: int = 0
    while mnbv < len(xyz):
        if len(xyz[mnbv]) == aabb:
            return xyz[mnbv]
        mnbv += 1