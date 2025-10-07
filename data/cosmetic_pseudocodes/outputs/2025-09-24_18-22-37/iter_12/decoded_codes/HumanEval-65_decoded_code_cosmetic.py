def circular_shift(int_val: int, num_shift: int) -> str:
    str_val: str = str(int_val)
    str_len: int = len(str_val)
    if num_shift > str_len:
        result_str: str = ''
        for idx in range(str_len, 0, -1):
            char_tmp: str = str_val[idx - 1]
            result_str += char_tmp
        return result_str
    else:
        cut_pos: int = str_len - num_shift
        part1: str = str_val[cut_pos:str_len]
        part2: str = str_val[0:cut_pos]
        final_str: str = part1 + part2
        return final_str