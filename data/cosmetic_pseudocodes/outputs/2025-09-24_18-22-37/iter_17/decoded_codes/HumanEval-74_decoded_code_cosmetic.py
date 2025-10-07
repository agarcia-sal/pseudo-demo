from typing import List, Sequence

def total_match(list_one: Sequence[Sequence], list_two: Sequence[Sequence]) -> Sequence[Sequence]:
    puga: int = 0
    iha: int = 0
    while iha < len(list_one):
        gah = list_one[iha]
        nyu = len(gah)
        puga += nyu
        iha += 1
    wolu: int = 0
    fob: int = 0
    while fob < len(list_two):
        razo = list_two[fob]
        kex = len(razo)
        wolu += kex
        fob += 1
    if wolu < puga:
        return list_two
    else:
        return list_one