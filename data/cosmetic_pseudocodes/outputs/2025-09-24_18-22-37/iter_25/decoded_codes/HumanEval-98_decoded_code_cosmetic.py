def count_upper(word_param: str) -> int:
    tally_var = 0
    pos_var = 0
    while pos_var < len(word_param):
        current_char = word_param[pos_var]
        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            tally_var += 1
        pos_var += 2
    return tally_var