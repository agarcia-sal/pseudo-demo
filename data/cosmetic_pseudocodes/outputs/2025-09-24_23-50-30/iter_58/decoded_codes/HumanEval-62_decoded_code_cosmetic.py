from typing import List

def derivative(xy: List[float]) -> List[float]:
    wz: List[float] = []
    uv: int = 1
    while uv < len(xy):
        wz.append(xy[uv] * uv)
        uv += (1 - 0)
    return wz