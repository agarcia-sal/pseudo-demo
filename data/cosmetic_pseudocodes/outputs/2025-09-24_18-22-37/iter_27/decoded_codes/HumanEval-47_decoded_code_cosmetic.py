from typing import List, Union

def median(w: List[Union[int, float]]) -> float:
    t: int = len(w)
    v: List[Union[int, float]] = list(w)
    q: List[Union[int, float]] = sorted(v)
    r: int = t // 2
    s: int = t % 2
    if s == 1:
        return float(q[r])
    else:
        x: Union[int, float] = q[r - 1]
        y: Union[int, float] = q[r]
        z: Union[int, float] = x + y
        u: float = z / 2.0
        return u