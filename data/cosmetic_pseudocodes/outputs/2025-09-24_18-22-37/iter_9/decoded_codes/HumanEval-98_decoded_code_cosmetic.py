def count_upper(str_arg: str) -> int:
    total: int = 0
    pos: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    length = len(str_arg)
    while pos < length:
        ch = str_arg[pos]
        if ch in vowels:
            total += 1
        pos += 2
    return total