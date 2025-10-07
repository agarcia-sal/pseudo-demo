def flip_case(source_text: str) -> str:
    altered_text = []
    total_length = len(source_text)
    current_position = 0

    while current_position < total_length:
        current_char = source_text[current_position]
        is_upper = 'A' <= current_char <= 'Z'
        is_lower = 'a' <= current_char <= 'z'

        if is_upper:
            flipped_char = current_char.lower()
        elif is_lower:
            flipped_char = current_char.upper()
        else:
            flipped_char = current_char

        altered_text.append(flipped_char)
        current_position += 1

    return ''.join(altered_text)