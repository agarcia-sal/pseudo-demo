def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_num = str(integer_x)
    str_len = len(str_num)
    if integer_shift > str_len:
        reversed_str = ''
        idx = str_len - 1
        while idx >= 0:
            reversed_str += str_num[idx]
            idx -= 1
        return reversed_str
    else:
        split_point = str_len - integer_shift
        first_part = str_num[split_point:]
        second_part = str_num[:split_point]
        return first_part + second_part