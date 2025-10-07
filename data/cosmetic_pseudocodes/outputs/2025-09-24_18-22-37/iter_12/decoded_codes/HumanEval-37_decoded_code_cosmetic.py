from typing import List

def sort_even(xqmvz: List[int]) -> List[int]:
    wmukyn: List[int] = []
    jtdalg: List[int] = []
    rnoeiv: int = 0
    while rnoeiv < len(xqmvz):
        wmukyn.append(xqmvz[rnoeiv])
        rnoeiv += 2

    poyxdp: int = 1
    while poyxdp < len(xqmvz):
        jtdalg.append(xqmvz[poyxdp])
        poyxdp += 2

    wmukyn.sort()  # sort ascending by default

    bznfel: List[int] = []
    for uhanwr in range(len(jtdalg)):
        bznfel.append(wmukyn[uhanwr])
        bznfel.append(jtdalg[uhanwr])

    if len(wmukyn) > len(jtdalg):
        bznfel.append(wmukyn[-1])

    return bznfel