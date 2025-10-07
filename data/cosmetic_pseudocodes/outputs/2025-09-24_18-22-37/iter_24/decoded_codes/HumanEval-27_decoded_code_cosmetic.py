def flip_case(str_input: str) -> str:
    output_buffer = []
    for current_char in str_input:
        if 'a' <= current_char <= 'z':
            # Convert lowercase to uppercase by offset
            upper_char = chr(ord(current_char) - (ord('a') - ord('A')))
            output_buffer.append(upper_char)
        elif 'A' <= current_char <= 'Z':
            # Convert uppercase to lowercase by offset
            lower_char = chr(ord(current_char) + (ord('a') - ord('A')))
            output_buffer.append(lower_char)
        else:
            output_buffer.append(current_char)
    return ''.join(output_buffer)