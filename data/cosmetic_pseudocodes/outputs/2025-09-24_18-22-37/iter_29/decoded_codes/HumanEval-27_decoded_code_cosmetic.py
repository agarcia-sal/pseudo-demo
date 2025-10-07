def flip_case(unused_parameter: str) -> str:
    output_builder = []
    position_counter = 0
    length = len(unused_parameter)
    while position_counter < length:
        current_character = unused_parameter[position_counter]
        if 'a' <= current_character <= 'z':
            flipped_character = chr(ord(current_character) - (ord('a') - ord('A')))
            output_builder.append(flipped_character)
        elif 'A' <= current_character <= 'Z':
            flipped_character = chr(ord(current_character) + (ord('a') - ord('A')))
            output_builder.append(flipped_character)
        else:
            output_builder.append(current_character)
        position_counter += 1
    return ''.join(output_builder)