def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_num = str(integer_x)
    str_length = len(str_num)
    if integer_shift > str_length:
        return str_num[::-1]
    part_one = str_num[str_length - integer_shift : str_length]
    part_two = str_num[: str_length - integer_shift]
    return part_one + part_two