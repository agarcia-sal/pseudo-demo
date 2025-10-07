def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_num: str = str(integer_x)
    n: int = len(str_num)
    if integer_shift > n:
        return str_num[::-1]
    split_point: int = n - integer_shift
    part_one: str = str_num[split_point:]
    part_two: str = str_num[:split_point]
    return part_one + part_two