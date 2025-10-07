def circular_shift(integer_x: int, integer_shift: int) -> str:
    num_str: str = str(integer_x)
    str_len: int = len(num_str)

    if integer_shift > str_len:
        # Return reversed string if shift is greater than length
        return num_str[::-1]

    pivot: int = str_len - integer_shift
    right_part: str = num_str[pivot:]
    left_part: str = num_str[:pivot]

    temp_str: str = right_part + left_part
    return temp_str