def encode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(char) + 5 - ord('a')) % 26) + ord('a')) for char in string_input
    )


def decode_shift(string_input: str) -> str:
    return ''.join(
        chr(((ord(char) - 5 - ord('a')) % 26) + ord('a')) for char in string_input
    )