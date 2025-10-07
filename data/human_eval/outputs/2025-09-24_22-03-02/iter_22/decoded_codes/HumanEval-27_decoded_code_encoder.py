def flip_case(string: str) -> str:
    result = []
    index = 0
    while index < len(string):
        char = string[index]
        if 'a' <= char <= 'z':
            flipped_char = char.upper()
        elif 'A' <= char <= 'Z':
            flipped_char = char.lower()
        else:
            flipped_char = char
        result.append(flipped_char)
        index += 1
    return ''.join(result)