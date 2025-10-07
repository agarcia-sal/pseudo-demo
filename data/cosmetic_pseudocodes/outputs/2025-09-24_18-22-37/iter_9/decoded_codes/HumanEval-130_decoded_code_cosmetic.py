from typing import List


def tri(param_m: int) -> List[int]:
    if param_m == 0:
        return [1]
    else:
        result_list: List[int] = [1, 3]

    counter_var = 2
    while counter_var - 1 < param_m:
        if counter_var % 2 == 0:
            temp_val = (counter_var // 2) + 1
            result_list.append(temp_val)
        else:
            idx1 = counter_var - 1
            idx2 = counter_var - 2
            temp_sum = result_list[idx1] + result_list[idx2]
            temp_div = (counter_var + 3) // 2
            combined_val = temp_sum + temp_div
            result_list.append(combined_val)
        counter_var += 1

    return result_list