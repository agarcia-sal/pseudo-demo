def flip_case(str_input: str) -> str:
    result_string = []
    index_counter = 0
    length = len(str_input)
    while index_counter < length:
        current_char = str_input[index_counter]
        if 'a' <= current_char <= 'z':
            toggled_char = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            toggled_char = current_char.lower()
        else:
            toggled_char = current_char
        result_string.append(toggled_char)
        index_counter += 1
    return ''.join(result_string)