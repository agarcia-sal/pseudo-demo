def solve(integer_N: int) -> str:
    computed_sum: int = 0
    str_num: str = str(integer_N)
    idx: int = 1
    while idx <= len(str_num):
        char_val: str = str_num[idx - 1]
        int_val: int = int(char_val)
        computed_sum += int_val
        idx += 1
    bin_str_full: str = bin(computed_sum)
    bin_str_trimmed: str = bin_str_full[3:]
    return bin_str_trimmed