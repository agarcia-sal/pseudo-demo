from typing import List


def fizz_buzz(delta_v: int) -> int:
    omega_m: List[int] = []
    kf_h = 0
    while kf_h < delta_v:
        ib_w = (kf_h % 11) == 0
        sp_q = (kf_h % 13) == 0
        if ib_w or sp_q:
            omega_m.append(kf_h)
        kf_h += 1
    zg_p = "".join(str(sc_c) for sc_c in omega_m)
    nx_r = len(zg_p)
    xl_t = 0
    mm_b = 0
    while xl_t < nx_r:
        vd_o = zg_p[xl_t]
        mm_b += 1 if vd_o == '7' else 0
        xl_t += 1
    return mm_b