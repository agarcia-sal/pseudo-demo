def flip_case(input_string: str) -> str:
    flipped_string = []
    index = 0
    length = len(input_string)
    while index < length:
        current_char = input_string[index]
        if 'a' <= current_char <= 'z':
            toggled_char = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            toggled_char = current_char.lower()
        else:
            toggled_char = current_char
        flipped_string.append(toggled_char)
        index += 1
    return ''.join(flipped_string)