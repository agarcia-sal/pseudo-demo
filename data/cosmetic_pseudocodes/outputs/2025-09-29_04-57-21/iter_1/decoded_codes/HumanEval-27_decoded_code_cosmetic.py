def flip_case(text: str) -> str:
    # Flip case of each character: lowercase to uppercase, others to lowercase
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in text)