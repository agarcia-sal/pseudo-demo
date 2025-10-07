def flip_case(input_string: str) -> str:
    return ''.join(c.lower() if c.isupper() else c.upper() for c in input_string)