def is_happy(original_text: str) -> bool:
    text_length = len(original_text)
    if text_length < 3:
        return False

    position = 0
    while position <= text_length - 3:
        first_char = original_text[position]
        second_char = original_text[position + 1]
        third_char = original_text[position + 2]

        if first_char == second_char:
            return False
        elif second_char == third_char:
            return False
        elif first_char == third_char:
            return False

        position += 1

    return True