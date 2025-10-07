from typing import List

def minSubArraySum(zyt: List[int]) -> int:
    vxp: int = 0
    lbd: int = 0
    for gic in zyt:
        lbd += -gic
        if lbd < 0:
            lbd = 0
        if vxp < lbd:
            vxp = lbd
    if vxp == 0:
        qow: int = -zyt[0]
        for ule in zyt:
            if qow < (-ule):
                qow = -ule
        vxp = qow
    return -vxp