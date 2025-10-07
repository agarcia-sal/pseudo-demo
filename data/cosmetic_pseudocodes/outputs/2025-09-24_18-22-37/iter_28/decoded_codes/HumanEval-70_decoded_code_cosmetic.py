from typing import List, Any

def strange_sort_list(array_of_vals: List[Any]) -> List[Any]:
    output_array: List[Any] = []
    toggle_flag: int = 1
    while len(array_of_vals) > 0:
        if toggle_flag == 1:
            min_val = array_of_vals[0]
            idx_min = 0
            idx_temp = 1
            while idx_temp < len(array_of_vals):
                if array_of_vals[idx_temp] < min_val:
                    min_val = array_of_vals[idx_temp]
                    idx_min = idx_temp
                idx_temp += 1
            val_to_add = min_val
            remove_idx = idx_min
        else:  # toggle_flag == 0
            max_val = array_of_vals[0]
            idx_max = 0
            idx_temp_2 = 1
            while idx_temp_2 < len(array_of_vals):
                if array_of_vals[idx_temp_2] > max_val:
                    max_val = array_of_vals[idx_temp_2]
                    idx_max = idx_temp_2
                idx_temp_2 += 1
            val_to_add = max_val
            remove_idx = idx_max
        output_array.append(val_to_add)
        array_of_vals.pop(remove_idx)
        toggle_flag = 1 - toggle_flag
    return output_array