def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_val = str(integer_x)
    if integer_shift > len(str_val):
        return str_val[::-1]
    split_point = len(str_val) - integer_shift
    return str_val[split_point:] + str_val[:split_point]