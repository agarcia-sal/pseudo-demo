def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_x = str(integer_x)
    len_str = len(str_x)
    if integer_shift > len_str:
        return str_x[::-1]  # Reverse the string if shift is greater than length
    split_point = len_str - integer_shift
    part1 = str_x[split_point:len_str]
    part2 = str_x[0:split_point]
    return part1 + part2