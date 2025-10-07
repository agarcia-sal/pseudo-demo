from typing import List


def words_string(str_param: str) -> List[str]:
    if str_param == "":
        return []

    buf_arr: List[str] = []
    idx_var: int = 0

    while idx_var < len(str_param):
        current_chr: str = str_param[idx_var]
        if current_chr == ",":
            buf_arr.append(" ")
        else:
            buf_arr.append(current_chr)
        idx_var += 1

    merged_str: str = ""
    iter_i: int = 0
    while iter_i < len(buf_arr):
        merged_str += buf_arr[iter_i]
        iter_i += 1

    return merged_str.split()