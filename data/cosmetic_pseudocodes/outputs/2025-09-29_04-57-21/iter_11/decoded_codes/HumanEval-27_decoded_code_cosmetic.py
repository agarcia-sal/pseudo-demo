def flip_case(input_string: str) -> str:
    result_string = []
    index_counter = 0

    while index_counter < len(input_string):
        current_char = input_string[index_counter]
        if current_char == current_char.lower():
            result_string.append(current_char.upper())
        else:
            result_string.append(current_char.lower())
        index_counter += 1

    return ''.join(result_string)