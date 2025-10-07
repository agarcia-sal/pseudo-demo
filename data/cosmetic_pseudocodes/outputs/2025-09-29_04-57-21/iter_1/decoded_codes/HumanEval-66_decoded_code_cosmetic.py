def digitSum(str_val: str) -> int:
    result_total: int = 0
    index: int = 0
    while index < len(str_val):
        current_char: str = str_val[index]
        if 'A' <= current_char <= 'Z':
            result_total += ord(current_char)
        index += 1
    return result_total