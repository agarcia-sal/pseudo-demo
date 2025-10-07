def flip_case(source_text: str) -> str:
    result_text = []
    for current_char in source_text:
        if 'a' <= current_char <= 'z':
            adjusted_char = current_char.upper()
            result_text.append(adjusted_char)
        elif 'A' <= current_char <= 'Z':
            adjusted_char = current_char.lower()
            result_text.append(adjusted_char)
        else:
            result_text.append(current_char)
    return ''.join(result_text)