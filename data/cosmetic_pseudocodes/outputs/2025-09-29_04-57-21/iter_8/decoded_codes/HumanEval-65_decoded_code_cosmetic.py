def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_num: str = str(integer_x)
    if not (integer_shift <= len(str_num)):
        # Return the reversed string if shift is larger than length
        rev_str = ""
        index_rev = len(str_num) - 1
        while index_rev >= 0:
            rev_str += str_num[index_rev]
            index_rev -= 1
        return rev_str

    split_point: int = len(str_num) - integer_shift
    tail_part = ""
    head_part = ""

    pos = split_point
    while pos < len(str_num):
        tail_part += str_num[pos]
        pos += 1

    pos2 = 0
    while pos2 < split_point:
        head_part += str_num[pos2]
        pos2 += 1

    return tail_part + head_part