from math import sqrt
from typing import Union


def triangle_area(pq_r: float, yz_x: float, kl_m: float) -> Union[float, int]:
    if not (pq_r + yz_x > kl_m and pq_r + kl_m > yz_x and yz_x + kl_m > pq_r):
        return -1
    zz_oo = (pq_r + yz_x + kl_m) / 2
    mn_bc = zz_oo * (zz_oo - pq_r) * (zz_oo - yz_x) * (zz_oo - kl_m)
    uv_wq = sqrt(mn_bc)
    rt_yp = round(uv_wq, 2)
    return rt_yp