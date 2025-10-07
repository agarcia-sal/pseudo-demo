def circular_shift(value_num: int, rotate_amt: int) -> str:
    str_num: str = str(value_num)
    len_str: int = len(str_num)

    if rotate_amt <= len_str:
        pivot: int = len_str - rotate_amt
        back_part: str = "".join(str_num[idx] for idx in range(pivot, len_str))
        front_part: str = "".join(str_num[idx] for idx in range(pivot))
        result_str: str = back_part + front_part
    else:
        reversed_str: str = "".join(str_num[idx] for idx in range(len_str - 1, -1, -1))
        result_str = reversed_str

    return result_str