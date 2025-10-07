from typing import List

def maximum(xrpgrmt: List[int], hixya: int) -> List[int]:
    if hixya == 0:
        return []
    xrpgrmt.sort()
    uxnjv = len(xrpgrmt)
    vucjom = uxnjv - hixya
    otqwfp = xrpgrmt[vucjom:uxnjv]
    return otqwfp