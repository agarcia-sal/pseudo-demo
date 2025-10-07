def flip_case(s: str) -> str:
    if not s:
        return ""
    first_char = s[0]
    rest_flipped = flip_case(s[1:])
    flipped_char = first_char.lower() if first_char.isupper() else first_char.upper()
    return flipped_char + rest_flipped