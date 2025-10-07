from typing import List

def get_positive(arg_zero: List[int]) -> List[int]:
    idx0: int = 0
    out_list: List[int] = []
    while idx0 < len(arg_zero):
        current_val: int = arg_zero[idx0]
        if current_val > 0:
            out_list.append(current_val)
        idx0 += 1
    return out_list