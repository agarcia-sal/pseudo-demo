def encode_shift(s: str) -> str:
    encoded_characters = []
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
        encoded_characters.append(chr(shifted_value))
    return ''.join(encoded_characters)

def decode_shift(s: str) -> str:
    decoded_characters = []
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
        decoded_characters.append(chr(shifted_value))
    return ''.join(decoded_characters)