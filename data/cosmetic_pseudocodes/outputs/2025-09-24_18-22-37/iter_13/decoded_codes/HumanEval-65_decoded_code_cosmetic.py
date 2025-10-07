def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str: str = str(integer_x)
    length_val: int = len(temp_str)
    if integer_shift > length_val:
        reversed_str: str = ""
        idx: int = length_val - 1
        while idx >= 0:
            reversed_str += temp_str[idx]
            idx -= 1
        return reversed_str
    else:
        split_point: int = length_val - integer_shift
        first_part: str = temp_str[split_point:length_val]
        second_part: str = temp_str[0:split_point]
        return first_part + second_part