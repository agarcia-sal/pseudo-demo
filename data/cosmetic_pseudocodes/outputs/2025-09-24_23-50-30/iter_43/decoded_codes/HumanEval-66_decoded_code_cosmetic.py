def digitSum(text_data: str) -> int:
    index_counter: int = 0
    ascii_accumulator: int = 0
    while index_counter < len(text_data):
        char_temp: str = text_data[index_counter]
        if 'A' <= char_temp <= 'Z':
            ascii_accumulator += ord(char_temp)
        else:
            ascii_accumulator += 0  # explicit no-op for non-uppercase letters
        index_counter += 1
    return ascii_accumulator