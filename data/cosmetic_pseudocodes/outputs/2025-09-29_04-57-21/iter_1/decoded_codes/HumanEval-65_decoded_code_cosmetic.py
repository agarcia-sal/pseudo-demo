def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_num = str(integer_x)
    str_length = len(str_num)
    if integer_shift > str_length:
        # reverse the string by iterating indices from end to start
        reversed_str = ''.join(str_num[i] for i in range(str_length - 1, -1, -1))
        return reversed_str
    else:
        cut_point = str_length - integer_shift
        part_one = str_num[cut_point:str_length]
        part_two = str_num[0:cut_point]
        return part_one + part_two