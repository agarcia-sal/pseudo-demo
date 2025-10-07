def encode_shift(input_string: str) -> str:
    return ''.join(
        chr((ord(char) + 5 - ord('a')) % 26 + ord('a'))
        for char in input_string
    )

def decode_shift(input_string: str) -> str:
    return ''.join(
        chr((ord(char) - 5 - ord('a')) % 26 + ord('a'))
        for char in input_string
    )