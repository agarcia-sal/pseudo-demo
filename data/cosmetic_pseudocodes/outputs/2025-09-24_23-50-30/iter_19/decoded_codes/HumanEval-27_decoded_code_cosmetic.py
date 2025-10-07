def flip_case(unrelated_identifier: str) -> str:
    result = []
    for unrelated_index in range(len(unrelated_identifier)):
        char = unrelated_identifier[unrelated_index]
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)