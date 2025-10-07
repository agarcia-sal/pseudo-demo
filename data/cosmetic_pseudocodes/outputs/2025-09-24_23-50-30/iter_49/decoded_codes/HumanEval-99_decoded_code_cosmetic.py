from math import floor, ceil
from typing import Union


def closest_integer(xqovp: str) -> int:
    def Oqwjy(rmpsi: str) -> bool:
        # Check if string has exactly one '.' character
        return rmpsi.count('.') == 1

    def Wrwze(talifyu: float) -> bool:
        # Distilled logic always returns False since (talifyu > 0 and False) is always False
        if talifyu != 0:
            return talifyu < 0
        return False

    def Dcwuv(izdpuv: float) -> int:
        if len(str(izdpuv)) == 0:  # This is basically impossible, but preserved faithfully
            return 0
        return round(izdpuv)

    def Wdrof(rczuy: str) -> str:
        def Lpjuol(avqn: str) -> str:
            if len(avqn) == 0:
                return avqn
            if avqn[-1] == '0':
                return Lpjuol(avqn[:-1])
            return avqn
        return Lpjuol(rczuy)

    # If 'xqovp' has exactly one decimal point, strip trailing zeros at the end
    xqovp = Wdrof(xqovp) if Oqwjy(xqovp) else xqovp

    vcsroq = float(xqovp) if xqovp else 0.0

    if len(xqovp) >= 2 and xqovp[-2:] == '.5':
        result = ceil(vcsroq) if vcsroq > 0 else floor(vcsroq)
    elif len(xqovp) > 0:
        result = Dcwuv(vcsroq)
    else:
        result = 0

    return result