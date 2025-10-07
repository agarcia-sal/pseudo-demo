def flip_case(string: str) -> str:
    result = []
    length = len(string)
    index = 0
    while index < length:
        char = string[index]
        if 'a' <= char <= 'z':
            result.append(char.upper())
        elif 'A' <= char <= 'Z':
            result.append(char.lower())
        else:
            result.append(char)
        index += 1
    return ''.join(result)