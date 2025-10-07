from typing import Union

def vowels_count(str_param: str) -> int:
    vow = "AEIOUaeiou"
    result_accum = 0
    for idx in range(len(str_param)):
        if str_param[idx] in vow:
            result_accum += 1
    if str_param and (str_param[-1] == 'Y' or str_param[-1] == 'y'):
        result_accum += 1
    return result_accum