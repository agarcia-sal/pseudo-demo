def count_upper(text_parameter: str) -> int:
    accumulator = 0
    position = 0
    while True:
        if position >= len(text_parameter):
            break
        current_char = text_parameter[position]
        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1
        position += 2
    return accumulator