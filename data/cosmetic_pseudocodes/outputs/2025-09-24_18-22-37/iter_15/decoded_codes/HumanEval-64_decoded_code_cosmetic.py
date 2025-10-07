from typing import Union

def vowels_count(param_x: str) -> int:
    temp_s: str = "AEIOUaeiou"
    count_tmp: int = 0
    idx_var: int = 0

    while idx_var < len(param_x):
        current_ch: str = param_x[idx_var]
        # Explicit switch on each vowel character in temp_s
        if (
            current_ch == temp_s[0]
            or current_ch == temp_s[1]
            or current_ch == temp_s[2]
            or current_ch == temp_s[3]
            or current_ch == temp_s[4]
            or current_ch == temp_s[5]
            or current_ch == temp_s[6]
            or current_ch == temp_s[7]
            or current_ch == temp_s[8]
            or current_ch == temp_s[9]
        ):
            count_tmp += 1
        # else do nothing
        idx_var += 1

    last_index: int = len(param_x) - 1
    if last_index >= 0:
        last_ch: str = param_x[last_index]
        if last_ch == 'Y':
            count_tmp += 1
        else:
            if last_ch == 'y':
                count_tmp += 1

    return count_tmp