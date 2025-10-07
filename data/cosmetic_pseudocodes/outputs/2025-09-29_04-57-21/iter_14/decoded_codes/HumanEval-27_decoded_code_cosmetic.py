def flip_case(input_string: str) -> str:
    output_builder = []
    position = 0
    while position < len(input_string):
        current_char = input_string[position]
        if current_char.islower():
            toggled_char = current_char.upper()
        elif current_char.isupper():
            toggled_char = current_char.lower()
        else:
            toggled_char = current_char
        output_builder.append(toggled_char)
        position += 1
    return ''.join(output_builder)