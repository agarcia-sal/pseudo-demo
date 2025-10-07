def count_upper(str_param: str) -> int:
    tally: int = 0
    position: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while position <= len(str_param) - 1:
        if str_param[position] in vowels:
            tally += 1
        position += 2
    return tally