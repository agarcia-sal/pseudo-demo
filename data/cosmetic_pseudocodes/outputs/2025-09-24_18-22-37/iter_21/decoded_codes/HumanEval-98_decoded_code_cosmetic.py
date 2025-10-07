def count_upper(str_param: str) -> int:
    tally = 0
    pos = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while pos < len(str_param):
        if str_param[pos] in vowels:
            tally += 1
        pos += 2
    return tally