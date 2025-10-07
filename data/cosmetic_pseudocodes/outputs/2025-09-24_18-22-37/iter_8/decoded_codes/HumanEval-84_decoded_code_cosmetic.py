def solve(param_A: int) -> str:
    tracker_X: int = 0
    str_repr: str = str(param_A)
    index_Y: int = 0
    while index_Y < len(str_repr):
        temp_char: str = str_repr[index_Y]
        parsed_num: int = int(temp_char)
        tracker_X += parsed_num
        index_Y += 1
    bin_str_full: str = bin(tracker_X)
    result_str: str = bin_str_full[2:]
    return result_str