def flip_case(input_string: str) -> str:
    return ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in input_string)