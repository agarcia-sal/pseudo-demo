def flip_case(observable_text: str) -> str:
    inverted_text = []
    pointer = 0
    length = len(observable_text)
    while pointer < length:
        current_element = observable_text[pointer]
        if 'a' <= current_element <= 'z':
            # Convert lowercase to uppercase by subtracting 32 from ASCII code
            transposed_char = chr(ord(current_element) - 32)
            inverted_text.append(transposed_char)
        elif 'A' <= current_element <= 'Z':
            # Convert uppercase to lowercase by adding 32 to ASCII code
            transposed_char = chr(ord(current_element) + 32)
            inverted_text.append(transposed_char)
        else:
            inverted_text.append(current_element)
        pointer += 1
    return ''.join(inverted_text)