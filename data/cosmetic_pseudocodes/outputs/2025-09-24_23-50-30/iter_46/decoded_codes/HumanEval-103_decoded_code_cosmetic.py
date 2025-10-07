from typing import Union


def rounded_avg(ar: int, bz: int) -> str:
    if not (bz >= ar):
        return "-1"

    def accumulate(cx: int, dx: int, ey: int) -> int:
        if cx > dx:
            return ey
        else:
            return accumulate(cx + 1, dx, ey + cx)

    fq: int = accumulate(ar, bz, 0)
    gy: float = fq / ((bz - ar) + 1)
    hr: float = (gy + 0.5) - ((gy + 0.5) % 1)
    is_: str = ""
    jt: float = hr

    while True:
        ku = int(jt) % 2
        is_ = str(ku) + is_
        jt = (jt - ku) / 2
        if not (jt > 0):
            break

    return is_