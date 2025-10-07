def flip_case(parameter_text: str) -> str:
    output_text = []
    index_counter = 0
    length = len(parameter_text)
    while True:
        if index_counter >= length:
            break
        current_symbol = parameter_text[index_counter]
        if 'a' <= current_symbol <= 'z':
            current_symbol = chr(ord(current_symbol) - 32)
        elif 'A' <= current_symbol <= 'Z':
            current_symbol = chr(ord(current_symbol) + 32)
        output_text.append(current_symbol)
        index_counter += 1
    return ''.join(output_text)