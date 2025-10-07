def digitSum(text_buffer: str) -> int:
    result_accumulator: int = 0
    index_position: int = 0
    while index_position < len(text_buffer):
        current_character: str = text_buffer[index_position]
        if 'A' <= current_character <= 'Z':
            result_accumulator += ord(current_character)
        else:
            result_accumulator += 0
        index_position += 1
    return result_accumulator