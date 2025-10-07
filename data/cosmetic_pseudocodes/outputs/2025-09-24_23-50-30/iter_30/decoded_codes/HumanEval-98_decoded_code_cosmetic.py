def count_upper(str_data: str) -> int:
    total: int = 0
    pos: int = 0
    while pos < len(str_data):
        if str_data[pos] in {'A', 'E', 'I', 'O', 'U'}:
            total += 1
        pos += 2
    return total