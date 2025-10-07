def flip_case(input_string: str) -> str:
    output_builder = []
    char_index = 1
    length = len(input_string)
    while char_index <= length:
        current_char = input_string[char_index - 1]
        if current_char.islower():
            output_builder.append(current_char.upper())
        elif current_char.isupper():
            output_builder.append(current_char.lower())
        else:
            output_builder.append(current_char)
        char_index += 1
    return ''.join(output_builder)