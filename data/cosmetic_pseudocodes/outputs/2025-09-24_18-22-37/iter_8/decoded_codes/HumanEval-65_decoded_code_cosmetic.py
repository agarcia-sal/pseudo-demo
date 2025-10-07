def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_value: str = str(integer_x)
    length_value: int = len(string_value)
    if integer_shift <= length_value:
        split_point: int = length_value - integer_shift
        left_part: str = string_value[:split_point]
        right_part: str = string_value[split_point:]
        return right_part + left_part
    else:
        return string_value[::-1]