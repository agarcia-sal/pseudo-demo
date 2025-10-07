def flip_case(input_string: str) -> str:
    result_builder = []
    for char in input_string:
        if char.isupper():
            result_builder.append(char.lower())
        elif char.islower():
            result_builder.append(char.upper())
        else:
            result_builder.append(char)
    return ''.join(result_builder)