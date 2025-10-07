def count_upper(string_param: str) -> int:
    acc: int = 0
    pos: int = 0
    while pos < len(string_param):
        if string_param[pos] in {'A', 'E', 'I', 'O', 'U'}:
            acc += 1
        pos += 2
    return acc