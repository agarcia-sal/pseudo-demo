def flip_case(str_input: str) -> str:
    output_buf = []
    length_val = len(str_input)
    idx_counter = 0
    while idx_counter < length_val:
        char_val = str_input[idx_counter]
        if 'A' <= char_val <= 'Z':
            output_buf.append(char_val.lower())
        elif 'a' <= char_val <= 'z':
            output_buf.append(char_val.upper())
        else:
            output_buf.append(char_val)
        idx_counter += 1
    return ''.join(output_buf)