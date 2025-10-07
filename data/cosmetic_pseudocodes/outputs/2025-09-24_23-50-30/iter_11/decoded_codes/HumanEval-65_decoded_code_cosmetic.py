def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_tmp = str(integer_x)
    if not (integer_shift <= len(str_tmp)):
        return str_tmp[::-1]
    len_tmp = len(str_tmp) - integer_shift
    return str_tmp[len_tmp:] + str_tmp[:len_tmp]