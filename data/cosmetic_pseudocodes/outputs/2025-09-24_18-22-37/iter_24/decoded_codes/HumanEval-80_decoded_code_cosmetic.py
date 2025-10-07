def is_happy(str_arg: str) -> bool:
    len_var = len(str_arg)
    if len_var < 3:
        return False
    pos_var = 0
    while pos_var <= len_var - 3:
        curr_char = str_arg[pos_var]
        next_char = str_arg[pos_var + 1]
        next_next_char = str_arg[pos_var + 2]
        if curr_char == next_char:
            return False
        if next_char == next_next_char:
            return False
        if curr_char == next_next_char:
            return False
        pos_var += 1
    return True