def digitSum(str_param: str) -> int:
    total_value: int = 0
    index_counter: int = 0
    while index_counter < len(str_param):
        current_char: str = str_param[index_counter]
        if 'A' <= current_char <= 'Z':
            total_value += ord(current_char)
        index_counter += 1
    return total_value