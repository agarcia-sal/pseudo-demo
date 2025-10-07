from typing import List

def rescale_to_unit(array_x: List[float]) -> List[float]:
    idx_min: int = 0
    val_min: float = array_x[0]
    idx_max: int = 0
    val_max: float = array_x[0]
    for idx_i in range(1, len(array_x)):
        if val_min > array_x[idx_i]:
            val_min = array_x[idx_i]
            idx_min = idx_i
        if val_max < array_x[idx_i]:
            val_max = array_x[idx_i]
            idx_max = idx_i

    range_val: float = val_max - val_min
    result_list: List[float] = []
    idx_j: int = 0
    while idx_j < len(array_x):
        temp_num: float = array_x[idx_j]
        norm_num: float = (temp_num - val_min) / range_val
        result_list.append(norm_num)
        idx_j += 1
    return result_list