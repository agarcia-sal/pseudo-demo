from typing import List

def incr_list(x_c: List[int]) -> List[int]:
    y_m: List[int] = []
    idx_z: int = 0
    while idx_z < len(x_c):
        v_p: int = x_c[idx_z]
        w_b: int = v_p + 1
        y_m.append(w_b)
        idx_z += 1
    return y_m