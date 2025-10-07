def flip_case(original_text: str) -> str:
    result_string = []
    position = 0
    length = len(original_text)
    while position < length:
        current_char = original_text[position]
        if current_char.islower():
            result_string.append(current_char.upper())
        elif current_char.isupper():
            result_string.append(current_char.lower())
        else:
            result_string.append(current_char)
        position += 1
    return ''.join(result_string)