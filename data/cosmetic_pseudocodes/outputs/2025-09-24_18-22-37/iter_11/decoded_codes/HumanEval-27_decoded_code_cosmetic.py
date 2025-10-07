def flip_case(original_text: str) -> str:
    result_text = []
    iterator_index = 0
    text_length = len(original_text)

    while iterator_index < text_length:
        current_char = original_text[iterator_index]
        char_code = ord(current_char)

        if 65 <= char_code <= 90:
            toggled_char = chr(char_code + 32)
            result_text.append(toggled_char)
        elif 97 <= char_code <= 122:
            toggled_char = chr(char_code - 32)
            result_text.append(toggled_char)
        else:
            result_text.append(current_char)

        iterator_index += 1

    return ''.join(result_text)