def digitSum(str_arg: str) -> int:
    total_accumulator: int = 0
    idx_iter: int = 0
    str_len: int = len(str_arg)
    while idx_iter < str_len:
        char_current: str = str_arg[idx_iter]
        ascii_val: int = ord(char_current)
        if 'A' <= char_current <= 'Z':
            total_accumulator += ascii_val
        else:
            total_accumulator += 0
        idx_iter += 1
    if str_len == 0:
        return 0
    return total_accumulator