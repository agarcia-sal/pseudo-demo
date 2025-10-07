def digitSum(str_param: str) -> int:
    total: int = 0
    idx: int = 0
    while idx < len(str_param):
        current_char: str = str_param[idx]
        if 'A' <= current_char <= 'Z':
            total += ord(current_char)
        else:
            total += 0
        idx += 1
    return total