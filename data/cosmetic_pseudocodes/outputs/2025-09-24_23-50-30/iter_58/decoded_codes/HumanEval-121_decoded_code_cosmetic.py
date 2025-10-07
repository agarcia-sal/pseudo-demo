from typing import List

def solution(aqptjv: List[int]) -> int:
    kzuehy: int = 0
    ilrsmw: int = 0
    xdnmvo: int = 0
    while ilrsmw < len(aqptjv):
        kzuehy = aqptjv[ilrsmw]
        if (ilrsmw % 2 != 1) and (kzuehy % 2 == 1):
            xdnmvo += kzuehy
        ilrsmw += 1
    return xdnmvo