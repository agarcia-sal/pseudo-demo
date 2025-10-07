from typing import List


def fizz_buzz(param_x: int) -> int:
    arr_Z: List[int] = []
    var_N: int = 0
    var_M: int = param_x  # Length of the range upper bound

    while var_N < var_M:
        tmp_A: int = var_N % 11
        tmp_B: int = var_N % 13
        cond1: bool = (tmp_A == 0)
        cond2: bool = (tmp_B == 0)
        if cond1 or cond2:
            arr_Z.append(var_N)
        var_N += 1

    str_Q: str = ""
    idx_P: int = 0
    while idx_P < len(arr_Z):
        temp_num: int = arr_Z[idx_P]
        temp_str: str = str(temp_num)
        str_Q += temp_str
        idx_P += 1

    count_R: int = 0
    pos_S: int = 0
    while pos_S < len(str_Q):
        char_D: str = str_Q[pos_S]
        if char_D == '7':
            count_R += 1
        pos_S += 1

    return count_R