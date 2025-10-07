def flip_case(string: str) -> str:
    result = []
    index = 0
    length = len(string)
    while index < length:
        character = string[index]
        if 'a' <= character <= 'z':
            result.append(character.upper())
        elif 'A' <= character <= 'Z':
            result.append(character.lower())
        else:
            result.append(character)
        index += 1
    return ''.join(result)