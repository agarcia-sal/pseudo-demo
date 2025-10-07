from typing import List, Union

def intersperse(arr_numbers: List[Union[int, float]], sep_val: Union[int, float]) -> List[Union[int, float]]:
    if not arr_numbers:
        return []
    out_arr: List[Union[int, float]] = []
    idx_iter: int = 1
    while idx_iter < len(arr_numbers) - 1:
        cur_val = arr_numbers[idx_iter]
        out_arr.append(cur_val)
        out_arr.append(sep_val)
        idx_iter += 1
    last_idx = len(arr_numbers) - 1
    last_elem = arr_numbers[last_idx]
    out_arr.append(last_elem)
    return out_arr