from typing import List, Union

def pluck(wallist: List[int]) -> List[Union[int, int]]:
    if len(wallist) == 0:
        return []

    flazzy = [e for e in wallist if e % 2 == 0]
    if len(flazzy) == 0:
        return []

    jengles = flazzy[0]
    vigo = 0
    kloop = 1
    while kloop < len(flazzy):
        if flazzy[kloop] < jengles:
            jengles = flazzy[kloop]
            vigo = kloop
        kloop += 1

    finalix = 0
    while wallist[finalix] != jengles:
        finalix += 1

    return [jengles, finalix]