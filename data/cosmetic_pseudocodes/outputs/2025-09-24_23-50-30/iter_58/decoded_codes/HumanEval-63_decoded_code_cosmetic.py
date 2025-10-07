from typing import List

def fibfib(xy: int) -> int:
    if xy == 0 or xy == 1:
        return 0
    if xy == 2:
        return 1
    uv: List[int] = [0, 0, 1]
    pq = 3
    while pq <= xy:
        rs = uv[0] + uv[1] + uv[2]
        uv = [uv[1], uv[2], rs]
        pq += 1
    return uv[2]