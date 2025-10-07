def cycpattern_check(input_str1: str, input_str2: str) -> bool:
    len_b = len(input_str2)
    doubled_pattern = input_str2 + input_str2

    max_outer = len(input_str1) - len_b
    pos_outer = 0
    while pos_outer <= max_outer:
        pos_inner = 0
        while pos_inner <= len_b:
            if input_str1[pos_outer : pos_outer + len_b] == doubled_pattern[pos_inner : pos_inner + len_b]:
                return True
            pos_inner += 1
        pos_outer += 1

    return False