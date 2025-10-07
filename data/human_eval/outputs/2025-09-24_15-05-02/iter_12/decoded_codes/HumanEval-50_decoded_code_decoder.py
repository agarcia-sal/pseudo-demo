def encode_shift(input_string: str) -> str:
    return ''.join(chr(((ord(character) + 5 - ord('a')) % 26) + ord('a')) for character in input_string)

def decode_shift(input_string: str) -> str:
    return ''.join(chr(((ord(character) - 5 - ord('a')) % 26) + ord('a')) for character in input_string)