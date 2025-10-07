def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_val = str(integer_x)
    if len(str_val) < integer_shift + 1:
        return str_val[::-1]
    return str_val[-integer_shift:] + str_val[:-integer_shift]