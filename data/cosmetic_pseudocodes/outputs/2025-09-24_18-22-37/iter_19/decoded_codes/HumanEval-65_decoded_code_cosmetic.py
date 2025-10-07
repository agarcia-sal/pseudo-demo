def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str: str = str(integer_x)
    str_len: int = len(temp_str)
    flag_exceed: bool = integer_shift > str_len
    if not flag_exceed:
        part_right_start: int = str_len - integer_shift
        right_part: str = temp_str[part_right_start:str_len]
        left_part: str = temp_str[:part_right_start]
        result: str = right_part + left_part
        return result
    else:
        rev_str: str = ''
        idx: int = str_len - 1
        while idx >= 0:
            rev_str += temp_str[idx]
            idx -= 1
        return rev_str