from typing import List

def sort_array(xyz: List[int]) -> List[int]:
    length: int = len(xyz)
    if length == 0:
        return []
    pqr: int = xyz[0] + xyz[-1]
    uvw: bool = (pqr % 2 == 0)
    return sorted(xyz, reverse=uvw)