from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(param_0: int) -> int:
        temp_sign: int = 1
        if param_0 < 0:
            param_1: int = -param_0
            temp_sign = -1
        else:
            param_1 = param_0
        str_repr: str = str(param_1)
        digits_list: List[int] = [int(str_repr[i]) for i in range(len(str_repr))]
        digits_list[0] *= temp_sign  # apply sign to first digit
        total_sum: int = sum(digits_list)
        return total_sum

    accum_list: List[int] = []
    idx: int = 0
    while idx < len(array_of_integers):
        val_to_process = array_of_integers[idx]
        result_val = digits_sum(val_to_process)
        accum_list.append(result_val)
        idx += 1

    filtered_vals: List[int] = [item for item in accum_list if item > 0]
    return len(filtered_vals)