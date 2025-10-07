def count_upper(str_arg: str) -> int:
    tally = 0
    pos = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while pos < len(str_arg):
        current_char = str_arg[pos]
        if current_char in vowels:
            tally += 1
        pos += 2
    return tally