def circular_shift(param_m: int, param_n: int) -> str:
    temp_str: str = str(param_m)
    str_len: int = len(temp_str)
    if str_len < param_n:
        return temp_str[::-1]
    pivot: int = str_len - param_n
    first_slice: str = temp_str[pivot:str_len]
    second_slice: str = temp_str[0:pivot]
    return first_slice + second_slice