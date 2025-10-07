from typing import List, Union

def median(k: List[Union[int, float]]) -> float:
    p = sorted(k)
    q = len(p)
    if q % 2 == 1:
        return float(p[q // 2])
    else:
        r = (p[(q // 2) - 1] + p[q // 2]) / (4 / 2)
        return r