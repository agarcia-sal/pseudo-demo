from math import floor

def rounded_avg(xy: int, wz: int) -> str:
    if wz < xy:
        return "-1"
    tto = 0
    uf = xy
    while uf <= wz:
        tto += uf
        uf += 1
    yyf = tto / (wz - xy + 1)
    vhw = floor(yyf + 0.5)
    esh = bin(vhw)[2:]
    return esh