def digitSum(text_param: str) -> int:
    result_accumulator: int = 0
    position_index: int = 0

    while position_index < len(text_param):
        current_char: str = text_param[position_index]
        if 'A' <= current_char <= 'Z':
            ascii_value: int = ord(current_char)
            result_accumulator += ascii_value
        else:
            result_accumulator += 0
        position_index += 1

    if len(text_param) == 0:
        result_accumulator = 0

    return result_accumulator