def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str = str(integer_x)
    len_str = len(temp_str)
    if integer_shift > len_str:
        return temp_str[::-1]
    else:
        part1 = temp_str[len_str - integer_shift : len_str]
        part2 = temp_str[: len_str - integer_shift]
        return part1 + part2