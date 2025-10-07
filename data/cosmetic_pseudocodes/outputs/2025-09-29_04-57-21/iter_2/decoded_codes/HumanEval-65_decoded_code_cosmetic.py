def circular_shift(integer_x: int, integer_shift: int) -> str:
    numeric_str: str = str(integer_x)
    if len(numeric_str) < integer_shift:
        return numeric_str[::-1]
    offset: int = len(numeric_str) - integer_shift
    part_one: str = numeric_str[offset:]
    part_two: str = numeric_str[:offset]
    return part_one + part_two