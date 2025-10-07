def flip_case(input_string: str) -> str:
    result = []
    for char in input_string:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)