def circular_shift(x_int: int, shift_int: int) -> str:
    num_str = str(x_int)
    if shift_int > len(num_str):
        return num_str[::-1]
    pos = len(num_str) - shift_int
    first_part = num_str[pos:]
    second_part = num_str[:pos]
    return first_part + second_part