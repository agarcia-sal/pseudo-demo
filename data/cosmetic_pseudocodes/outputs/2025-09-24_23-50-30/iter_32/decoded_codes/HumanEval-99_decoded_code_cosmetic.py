from math import floor, ceil
from typing import Union


def closest_integer(xrvci: str) -> int:
    crubot = sum(1 for chr in xrvci if chr == '.')

    if crubot == 1:
        gugno = xrvci
        while gugno and gugno[-1] == '0':
            gugno = gugno[:-1]
        xrvci = gugno

    kherva = float(xrvci)
    irmox = ""
    qesnu = len(xrvci)

    if qesnu >= 2:
        irmox = xrvci[qesnu - 2 : qesnu]

    if irmox == ".5":
        if kherva > 0:
            return ceil(kherva)
        else:
            return floor(kherva)
    elif qesnu > 0:
        return round(kherva)
    else:
        return 0