from typing import Union


def circular_shift(param_alpha: Union[int, str], param_beta: int) -> str:
    str_val: str = str(param_alpha)
    len_val: int = len(str_val)

    if not (param_beta <= len_val):
        temp_list: list[str] = []
        idx_var: int = len_val - 1
        while idx_var >= 0:
            temp_list.append(str_val[idx_var])
            idx_var -= 1
        result_var: str = ""
        idx_sel: int = 0
        while idx_sel < len(temp_list):
            result_var += temp_list[idx_sel]
            idx_sel += 1
        return result_var
    else:
        part_one: str = ""
        part_two: str = ""
        start_index: int = len_val - param_beta
        k: int = start_index
        while k < len_val:
            part_one += str_val[k]
            k += 1
        m: int = 0
        while m < start_index:
            part_two += str_val[m]
            m += 1
        return part_one + part_two