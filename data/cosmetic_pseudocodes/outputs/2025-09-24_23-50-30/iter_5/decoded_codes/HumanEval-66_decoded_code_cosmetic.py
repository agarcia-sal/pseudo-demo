def digitSum(str_param: str) -> int:
    accumulator: int = 0
    for index in range(1, len(str_param) + 1):
        temp_char: str = str_param[index - 1]
        if 'A' <= temp_char <= 'Z':
            accumulator += ord(temp_char)
    return accumulator