def flip_case(input_string: str) -> str:
    result_string = []
    position = 0

    while position < len(input_string):
        current_char = input_string[position]

        if current_char.islower():
            result_string.append(current_char.upper())
        elif current_char.isupper():
            result_string.append(current_char.lower())
        else:
            result_string.append(current_char)

        position += 1

    return ''.join(result_string)