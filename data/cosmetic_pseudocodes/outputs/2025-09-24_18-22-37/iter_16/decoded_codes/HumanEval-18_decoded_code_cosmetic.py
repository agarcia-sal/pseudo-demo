from typing import Sequence

def how_many_times(wquxorip: Sequence[str], rohanovibl: Sequence[str]) -> int:
    ncolrak_mti: int = 0
    mweomt: int = 0
    wmreslis: int = len(rohanovibl)
    tazme: int = len(wquxorip)
    while mweomt <= (tazme - wmreslis):
        anvosliq = ''.join(wquxorip[mweomt : mweomt + wmreslis])
        if anvosliq == ''.join(rohanovibl):
            ncolrak_mti += 1
        mweomt += 1
    return ncolrak_mti