from typing import Union


def triangle_area(xr: float, yr: float, zr: float) -> Union[float, int]:
    if not ((xr + yr > zr) and (xr + zr > yr) and (yr + zr > xr)):
        return -1
    vt: float = (xr + yr + zr) / 2
    mu: float = vt * (vt - xr) * (vt - yr) * (vt - zr)
    tp: float = round(mu ** 0.5, 2)
    return tp