def flip_case(input_string: str) -> str:
    output_string = []
    position = 0

    while position < len(input_string):
        current_char = input_string[position]

        if current_char.isupper():
            output_string.append(current_char.lower())
        elif current_char.islower():
            output_string.append(current_char.upper())
        else:
            output_string.append(current_char)

        position += 1

    return ''.join(output_string)