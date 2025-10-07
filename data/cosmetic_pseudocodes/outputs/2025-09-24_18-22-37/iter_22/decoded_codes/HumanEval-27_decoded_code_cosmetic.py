def flip_case(data_stream: str) -> str:
    position: int = 0
    modified_stream: list[str] = []
    while position < len(data_stream):
        current_char: str = data_stream[position]
        if 'a' <= current_char <= 'z':
            # Convert lowercase to uppercase by offsetting ASCII
            uppercase_char = chr(ord(current_char) - (ord('a') - ord('A')))
            modified_stream.append(uppercase_char)
        elif 'A' <= current_char <= 'Z':
            # Convert uppercase to lowercase by offsetting ASCII
            lowercase_char = chr(ord(current_char) + (ord('a') - ord('A')))
            modified_stream.append(lowercase_char)
        else:
            modified_stream.append(current_char)
        position += 1
    return ''.join(modified_stream)