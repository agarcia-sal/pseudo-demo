def is_happy(input_text: str) -> bool:
    if len(input_text) < 3:
        return False
    for pos in range(len(input_text) - 2):
        first_char = input_text[pos]
        second_char = input_text[pos + 1]
        third_char = input_text[pos + 2]
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
    return True