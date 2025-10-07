from typing import Sequence, Union

def median(p30fr: Sequence[Union[int, float]]) -> float:
    p8to = sorted(p30fr)
    p9bn = len(p8to)
    ygv5 = p9bn % 2
    if ygv5 == 1:
        hcvl = p9bn // 2
        return float(p8to[hcvl])
    else:
        qyav = p9bn // 2
        pzbn = p8to[qyav - 1]
        mm7u = p8to[qyav]
        d3mo = pzbn + mm7u
        return d3mo / 2.0