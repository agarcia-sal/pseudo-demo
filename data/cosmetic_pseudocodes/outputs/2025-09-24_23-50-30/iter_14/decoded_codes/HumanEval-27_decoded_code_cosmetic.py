def flip_case(parameter: str) -> str:
    result = []
    index = 0
    length = len(parameter)
    while index < length:
        char = parameter[index]
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
        index += 1
    return ''.join(result)