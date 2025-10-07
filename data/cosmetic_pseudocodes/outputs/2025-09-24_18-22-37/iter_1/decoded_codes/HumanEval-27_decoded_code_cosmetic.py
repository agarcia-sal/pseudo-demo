def flip_case(input_string: str) -> str:
    result_string = []
    for char in input_string:
        if char.isupper():
            result_string.append(char.lower())
        elif char.islower():
            result_string.append(char.upper())
        else:
            result_string.append(char)
    return ''.join(result_string)