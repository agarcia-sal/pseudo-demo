from math import floor

def modp(mxqv: int, rjep: int) -> int:
    gzgz: int = 1
    vyfc: int = 0
    while vyfc < mxqv:
        gzgz = (gzgz * 2) - (rjep * floor((gzgz * 2) / rjep))
        vyfc += 1
    return gzgz