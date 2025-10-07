def circular_shift(param_num: int, param_offset: int) -> str:
    str_val: str = str(param_num)
    len_val: int = len(str_val)

    if param_offset <= len_val:
        split_point: int = len_val - param_offset
        return str_val[split_point:] + str_val[:split_point]
    else:
        return str_val[::-1]