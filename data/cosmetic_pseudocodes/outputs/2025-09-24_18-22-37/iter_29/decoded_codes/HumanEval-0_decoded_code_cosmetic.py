from typing import Sequence

def has_close_elements(xyz_list: Sequence[float], alpha_thresh: float) -> bool:
    p_cnt: int = 0
    length: int = len(xyz_list)
    while p_cnt < length:
        q_ind: int = 0
        while q_ind < length:
            if p_cnt != q_ind:
                val1: float = xyz_list[p_cnt]
                val2: float = xyz_list[q_ind]
                diff_abs: float = val1 - val2
                if diff_abs < 0:
                    diff_abs = -diff_abs
                if diff_abs < alpha_thresh:
                    return True
            q_ind += 1
        p_cnt += 1
    return False