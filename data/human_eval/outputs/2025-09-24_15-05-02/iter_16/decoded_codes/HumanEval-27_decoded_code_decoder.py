def flip_case(input_string: str) -> str:
    return ''.join(char.lower() if char.isupper() else char.upper() for char in input_string)