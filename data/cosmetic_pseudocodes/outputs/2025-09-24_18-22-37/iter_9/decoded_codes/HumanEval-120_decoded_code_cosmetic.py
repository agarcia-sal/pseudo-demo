from typing import List, Any

def maximum(xqv: List[Any], fwn: int) -> List[Any]:
    agn: int = 0
    if fwn != 0:
        ihb: int = len(xqv)
        xqv_sorted = sorted(xqv)
        agn = ihb - fwn
        return xqv_sorted[agn:ihb]
    else:
        return []