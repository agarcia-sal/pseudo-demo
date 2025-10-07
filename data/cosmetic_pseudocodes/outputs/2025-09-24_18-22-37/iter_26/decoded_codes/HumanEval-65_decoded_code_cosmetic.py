def circular_shift(a_number: int, a_shift: int) -> str:
    num_as_str = str(a_number)
    str_len = len(num_as_str)

    if a_shift > str_len:
        return num_as_str[::-1]

    split_point = str_len - a_shift
    right_part = num_as_str[split_point:]
    left_part = num_as_str[:split_point]

    return right_part + left_part