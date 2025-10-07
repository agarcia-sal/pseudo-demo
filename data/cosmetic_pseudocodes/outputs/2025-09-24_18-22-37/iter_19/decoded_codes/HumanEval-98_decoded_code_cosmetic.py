def count_upper(param_str: str) -> int:
    accum_var: int = 0
    iter_idx: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while True:
        if not (iter_idx >= len(param_str)):
            curr_ch = param_str[iter_idx]
            if curr_ch in vowels:
                accum_var += 1
            iter_idx += 2
        else:
            break
    return accum_var