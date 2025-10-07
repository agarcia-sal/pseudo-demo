def flip_case(original_text: str) -> str:
    transformed_text = ''
    position_counter = 1
    while position_counter <= len(original_text):
        current_char = original_text[position_counter - 1]  # Adjust for zero-based indexing
        if 'A' <= current_char <= 'Z':
            current_char = current_char.lower()
        elif 'a' <= current_char <= 'z':
            current_char = current_char.upper()
        transformed_text += current_char
        position_counter += 1
    return transformed_text